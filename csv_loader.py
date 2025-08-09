from langchain_community.document_loaders import CSVLoader
    
loader = CSVLoader(file_path='csv_sample.csv')

docs = loader.load()

print(docs[0])
print(len(docs))