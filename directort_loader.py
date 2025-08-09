from langchain_community.document_loaders import PyPDFLoader, DirectoryLoader

loader =  DirectoryLoader(
    path = 'books',
    glob = '*.pdf',
    loader_cls= PyPDFLoader

)

docs = loader.load()

print(docs[13].page_content)
print(docs[13].metadata)
print(len(docs))