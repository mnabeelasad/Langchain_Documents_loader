from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import PyPDFLoader


loader = PyPDFLoader('F:\projects for job\Generative AI\Introduction to neural signal analysis 21.01.2024.pdf')

docs = loader.load()

print(docs[2].metadata)
print (len(docs))
