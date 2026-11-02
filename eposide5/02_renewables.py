from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_templete = ChatPromptTemplate.from_messages([
    ("system","you are a friendly {subject} teacher, explain the simply in under 50words, with one reallife example."),
    ("human","{question}")
])

prompt = prompt_templete.invoke({"subject":"physics",
                                 "question":"what is gravity"}
                                 )
modelname = "llama3.2:latest"

llm = ChatOllama(model=modelname)

response = llm.invoke(prompt)
parser = StrOutputParser()
response = parser.invoke(response)

print(response)