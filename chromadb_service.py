import os
# from langchain_community.vectorstores import Chroma
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
import shutil
load_dotenv()

def load_chunks(docs):
    embeddings = OpenAIEmbeddings( #embedding function to convert text to vector 0s and 1s
        model = 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory= "./chromadb",
        embedding_function= embeddings,
        collection_name= "test_collection" #text collection name should always be small alphabets and no special characters
    )

    Chroma.add_documents(vectorstore, docs)
    # print("document added to chromadb")
    
def retriver(question):
    embeddings = OpenAIEmbeddings(
        model= 'text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory= "./chromadb",
        embedding_function= embeddings,
        collection_name= "test_collection"
    )
    # docs = vectorstore.similarity_search_with_relevance_scores(question, 3)
    docs = vectorstore.similarity_search(question, 5)
    return docs
# documents = retriver("What is parallel computing?")
# for i in documents:
#     print(i)
#     print("\n")