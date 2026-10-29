from langchain_ollama import ChatOllama

modelname = "llama3.2:latest"

llm = ChatOllama(model=modelname)

response = llm.invoke("what is AI")

print(response.content)