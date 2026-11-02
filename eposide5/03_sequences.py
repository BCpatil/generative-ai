from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt_templete = ChatPromptTemplate.from_messages([
    ("system","you are a friendly {subject} teacher, explain the simply in under 50words, with one reallife example."),
    ("human","{question}")
])


llm = ChatOllama(model="llama3.2:latest")


parser = StrOutputParser()

chain = prompt_templete | llm | parser

for chunk in chain.stream({"subject":"physics",
                        "question":"what is gravity"} ):
    print(chunk, end="",flush=True)