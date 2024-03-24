import os
from langchain.prompts import PromptTemplate, FewShotPromptTemplate
from langchain_openai import OpenAI
from langchain.chains import LLMChain

open_key = os.environ['OPENAI_API_KEY']

llm = OpenAI(api_key=open_key,temperature=0.7)


exemples = [
    {"word": "happy", "antonym": "sad"},
    {"word": "tall", "antonym": "short"}
]

template = '''word: {word}
Antonym: {antonym}'''

prompt = PromptTemplate(
    input_variables=["word", "antonym"],
    template=template
)

fewshotprompt = FewShotPromptTemplate( 
    examples=exemples,
    example_prompt=prompt,
    prefix="Give the antonym of every imput\n",
    suffix="Word: {input}\nAntonym: ",
    input_variables=['input'],
    example_separator="\n"
)

chain=LLMChain(llm=llm,prompt=fewshotprompt)
print(chain.invoke({"input":"Big"}))