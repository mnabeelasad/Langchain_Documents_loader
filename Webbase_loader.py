from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model_name='gpt-3.5-turbo')

prompt = PromptTemplate(

     template = 'Answer the following question \n {Question} from the following text - \n {text}',
     input_variables=['Question','text']   
)

parser = StrOutputParser()


url = 'https://www.news18.com/cricket/pakistan-vs-west-indies-live-score-1st-odi-pak-vs-wi-match-latest-cricket-scorecard-brian-lara-stadium-trinidad-liveblog-ws-l-9494021.html'
loader  = WebBaseLoader(url)

docs = loader.load()

chain = prompt | model | parser

print(chain.invoke({'Question': 'Who was the player of the Match and other how many players perfoms good?', 'text': docs[0].page_content}))