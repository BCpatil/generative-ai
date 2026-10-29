from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage , HumanMessage

messages = [
    ("system","you are a funny auto driver in bengaluru and give a replay in one line "),
    HumanMessage("what is IT company ")
]

modelname = "llama3.2:latest"

llm = ChatOllama(model=modelname)

response = llm.invoke("what is IT company")

print(response.content)