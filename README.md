# End-to-end-Medical-Chatbot-using-Llama2

## Steps to run the project

'''bash
conda create -n mchatbot python=3.10 -y
'''

'''bash
conda activate mchatbot
'''


'''bash
pip install -r requirements.txt
'''

# To run the code:
### STEPS:

Clone the repository

'''bash
Project repo: https://github.com/entbappy/End-to0end-Medical-Chatbot-using-Llama2
'''

### STEP 01- Create a conda environment after opening the repository

'''bash
conda create -n mchatbot python=3.8 -y
'''

'''bash
conda activate mchatbot
'''

### STEP 02-INSTALL THE REQUIREMENTS
'''bash
pip install -r requirements.txt
'''

### Create a '.env' file in the root directory and add your Pinecone credentials as follows"

'''ini
PINECONE_API_KEY = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
PINECONE_API_ENV = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
'''

### Download the quantized model from the link provided in model folder & keep the model in rhe model directory:

'''ini
## Download the Llama 2 Model:

llama-2-7b-chat.ggmlv3.q4_0.bin

## From the following link:
https://huggingface.co/TheBloke/Llama-2-7B-Chat-GGML/tree/main


'''bash
# run the following command
python store_index.py
'''

'''bash
# Finally run the following command
python app.py
'''

### Techstack Used:
- Python
- LangChain
- Flask
- Meta Llama
- Pinecone



