from src.helper import load_pdf, text_split, download_huggingface_embedding_model
from langchain_pinecone import PineconeVectorStore
from dotenv import load_dotenv
from pinecone import Pinecone, ServerlessSpec
import os

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')

print('pinecone api key:', PINECONE_API_KEY)

# Extract data from PDF
extracted_data = load_pdf("data/")

# Create text chunks
text_chunks = text_split(extracted_data)

# Download embeddings model
embeddings = download_huggingface_embedding_model()

# Initialize Pinecone
pc = Pinecone(api_key=PINECONE_API_KEY)

# Index name
index_name = "medical-bot"

# Check if index exists, if not create it
if index_name not in pc.list_indexes().names():
    pc.create_index(
        name=index_name,
        dimension=384,  # dimension for all-MiniLM-L6-v2
        metric='cosine',
        spec=ServerlessSpec(
            cloud='aws',
            region='us-east-1'  # change to your preferred region
        )
    )

# Create vector store and add texts
docsearch = PineconeVectorStore.from_documents(
    documents=text_chunks,
    embedding=embeddings,
    index_name=index_name
)

print("Indexing complete.")