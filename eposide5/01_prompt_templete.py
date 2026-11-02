from langchain_ollama import ChatOllama
from langchain_core.prompts import ChatPromptTemplate

prompt_templete = ChatPromptTemplate.from_messages([
    ("system","you are a friendly {subject} teacher, explain the simply in under 50words, with one reallife example."),
    ("human","{question}")
])

prompt = prompt_templete.invoke({"subject":"KANNADA",
                                 "question":"what is KANNADA"}
                                 )
modelname = "llama3.2:latest"

llm = ChatOllama(model=modelname)

response = llm.invoke(prompt)

print(response.content)