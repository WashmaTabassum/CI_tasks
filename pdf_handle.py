from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from chromadb_service import load_chunks
import logging

# logging.basicConfig(level=logging.DEBUG,
#                     format='%(asctime)s - %(levelname)s - %(message)s',
#                     filename='pdf_handle.log'
#                     )
# logging.debug("This is a debug message")
# logging.info("This is an info message")
# logging.warning("This is a warning message")
# logging.error("This is an error message")
# logging.critical("This is a critical message")

loader = PyPDFLoader("./Lecture 01 - Introduction to Parallel and Distributed Computing.pdf")
docs = loader.load()

# print(docs[0])
# print("length of pdf/pages",len(docs))
#function to split the text in 50 chunks
splitter = RecursiveCharacterTextSplitter(
    chunk_size = 20,
    chunk_overlap = 20,
    length_function=len,
    is_separator_regex=False
)
#takes content from page_content variable and call splitter function to split text in 50s and store in chunks list
chunks = []
for item in docs:
    text = item.page_content
    pieces = splitter.create_documents([text])
    chunks.extend(pieces)
# logging.warning(len(chunks))
load_chunks(chunks)
# print(chunks[0])
# print(len(chunks))