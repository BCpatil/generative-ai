from langchain_ollama import ChatOllama

modelname  = "llama3.2:latest"

temperature = [ 0 , 0.5 , 1.2]
for temp in temperature:
    llm = ChatOllama(model=modelname,temperature=1.2)

    response = llm.invoke("what is Ai in one line")

    print(f"Temperature: {temp} ,output {response.content}")