from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name='gpt-3.5-turbo')

prompt = PromptTemplate(

     template = 'Write a very short summary of the following text: {text}',
     input_variables=['text']   
)

parser = StrOutputParser()

loader = TextLoader('cricket.txt', encoding="utf-8")
docs = loader.load()


# print(docs[0].page_content)
# print(type(docs))
# print(len(docs))


chain = prompt | model | parser

print(chain.invoke({'text': docs[0].page_content}))