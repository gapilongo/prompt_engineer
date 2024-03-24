import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

open_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_key=open_key,temperature=0.7)

template = ''' You are code expert and i need you to act like software engineer. in an easy way explain basics of {request}'''

prompt=PromptTemplate(
    input_variables=['request'],
    template=template
)


chain=LLMChain(llm=llm, prompt=prompt)
print(chain.invoke('sum function with python')['text'])