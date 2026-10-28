import ollama
message = [

    {
        "role":"system",
        "content":"you are a funny bengaluru auto driver , replay in one line"
    },
    {
        "role":"user",
        "content":"what is AI ? "
    }
]

modelname="llama3.2:latest"
response=ollama.chat(
    model=modelname,
    messages=message
)

print(response.message.content)