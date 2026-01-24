from flask import Flask, render_template, jsonify, request
from src.helper import download_huggingface_embedding_model
from pinecone import Pinecone, ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import CTransformers
from langchain_classic.chains import RetrievalQA  # Fixed import
from dotenv import load_dotenv
from src.prompt import *  # Import everything from the prompt.py file
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

embeddings = download_huggingface_embedding_model()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Index name
index_name = "medical-bot"

# Load INDEX FROM PINECONE ALREADY CREATED IN STORE.PY
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name, 
    embedding=embeddings
)

PROMPT = PromptTemplate(
    template=prompt_template,
    input_variables=["context", "question"]
)

chain_type_kwargs = {"prompt": PROMPT}

llm = CTransformers(
    model="model/llama-2-7b-chat.ggmlv3.q4_0.bin", 
    model_type="llama",
    config={"temperature": 0.8, "max_new_tokens": 512}
)

# Initialize the RetrievalQA bot
qa = RetrievalQA.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=docsearch.as_retriever(search_kwargs={"k": 2}),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)


# Default route - serves the chat interface
@app.route("/")
def home():
    return render_template("chat.html") 


# Chat endpoint - handles user messages
@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input_text = msg
    print(f"User Input: {input_text}")
    result = qa({"query": input_text})
    print(f"Response: {result['result']}")
    return str(result["result"])


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)