import os
import string
from langchain.indexes import VectorstoreIndexCreator
from langchain.chains import ConversationalRetrievalChain
from langchain_community.document_loaders import TextLoader
from langchain_community.chat_models import ChatOpenAI

# OpenAI API integration function
def openai_integration(question, file_name):
    # Define OpenAI API key
    os.environ["OPENAI_API_KEY"] = "api_key"
    
    # Load File
    loader = TextLoader(file_name, encoding='utf-8')
    loader.load()

    # Vectorize Data
    index = VectorstoreIndexCreator().from_loaders([loader])

    # Create Chain with OpenAI Model
    chain = ConversationalRetrievalChain.from_llm(llm=ChatOpenAI(model="gpt-3.5-turbo"), retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}))
    
    # Processing question before calling OpenAI
    question = process_question(question)
    result = chain({"question": question, "chat_history": []})
    return result['answer']

# Process User's input question function
def process_question(question):
    # Convert to lowercase
    question = question.lower()
    
    # Remove punctuation
    question = question.translate(str.maketrans('', '', string.punctuation))
    
    # Remove leading and trailing whitespaces
    question = question.strip()
    
    return question