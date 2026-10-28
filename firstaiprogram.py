
import ollama
modelname="llama3.2:latest"
prompt="Explain how AI works in one line"
response = ollama.generate(
    model=modelname,
    prompt=prompt)

print(response.response)

