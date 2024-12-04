# # chat service with chroma
# import os
# import shutil
# from dotenv import load_dotenv
# from langchain_chroma import Chroma
# from langchain_openai import OpenAIEmbeddings,ChatOpenAI
# from langchain_core.output_parsers import StrOutputParser
# from langchain_core.runnables import RunnablePassthrough
# from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
# load_dotenv()



# def load_chunks(docs):
#     embeddings = OpenAIEmbeddings()
#     vectorstore = Chroma(
#         persist_directory="./chromadb",
#         embedding_function=embeddings,
#         collection_name="test_collection",
#     )
#     print("Adding documents to vectorstore")
#     Chroma.add_documents(vectorstore, docs)
#     print("Documents added to vectorstore")

# def get_retriver():
#     embeddings = OpenAIEmbeddings(
#         model='text-embedding-ada-002'
#     )
#     vectorstore = Chroma(
#         persist_directory="./chromadb",
#         embedding_function=embeddings,
#         collection_name="test_collection",
#     )

#     return vectorstore.as_retriever()

# def format_docs(docs):
#     return "\n\n".join(doc.page_content for doc in docs)




# LLM = ChatOpenAI(model='gpt-4o-mini')
# retriver = get_retriver()
# prompt = ChatPromptTemplate.from_template(
#     """You can answer any question from this data
#     {data}

#     This is the question: {question}
#     """
# )
# chain = ( 
#     {"data": retriver | format_docs, "question": RunnablePassthrough()}
#     | prompt 
#     | LLM 
#     | StrOutputParser())

# print(chain.invoke("what is hydrogen fuel cell?"))





# response = chain.stream({"question": "dogs"})
# for r in response:
#     print(r, end="",flush=True)

# import os
# from dotenv import load_dotenv
# load_dotenv()

# from langchain_openai import ChatOpenAI
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# LLM = ChatOpenAI(model = 'gpt-4o-mini')
# prompt = ChatPromptTemplate.from_template(
#     """ you can tell jokes about any topic
#       this is topic :{question}
# """
# )

# chain = prompt | LLM | StrOutputParser()

# print(chain.invoke({'question': "dogs"}))

# response = chain.stream({'question': "dogs"})

# for r in response:
#     print(r, end="",flush=True)





#sir 
# chat service with chroma
import os
import shutil
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_openai import OpenAIEmbeddings,ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

load_dotenv()

def load_chunks(docs):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="test_collection",
    )
    print("Adding documents to vectorstore")
    Chroma.add_documents(vectorstore, docs)
    print("Documents added to vectorstore")

def get_retriver():
    embeddings = OpenAIEmbeddings(
        model='text-embedding-ada-002'
    )
    vectorstore = Chroma(
        persist_directory="./chromadb",
        embedding_function=embeddings,
        collection_name="test_collection",
    )

    return vectorstore.as_retriever()

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

SYSTEM_TEMPLATE = """
    Answer the user's questions based on the below context. 

    <context>
    {context}
    </context>

    This is the user question: {question}
    """

model = ChatOpenAI(model='gpt-4o-mini')
prompt = ChatPromptTemplate.from_template(SYSTEM_TEMPLATE)
retriver = get_retriver()

chain = (
    {"context": retriver | format_docs, "question": RunnablePassthrough()}
    | prompt
    | model
    | StrOutputParser()
)


# response = chain.invoke("what is hydrogen fuel cell")
# print(response)


# # if you want to stream the response do this 
# response = chain.stream("what is hydrogen fuel cell")
# for i in response:
#     print(i , end="" , flush=True)