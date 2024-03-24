import os
from langchain.prompts import PromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

open_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_key=open_key,temperature=0.7)

template = '''Translate the following sentence '{sentance}' into {target_language}'''

prompt=PromptTemplate(
    input_variables=['sentance', 'target_language'],
    template=template
)

chain=LLMChain(llm=llm,prompt=prompt)

print(chain.invoke({'sentance':'Hello, where are you?','target_language':'french'})['text'])
