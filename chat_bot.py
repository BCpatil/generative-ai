
import ollama

messages = [
    {"role": "system", "content": "You are a friendly assistant"}
]

while True:
    user_prompt = input("YOU: ")

    if user_prompt.lower() == "exit":
        print("Assistant: Goodbye! 👋")
        break

    user_role = {"role": "user", "content": user_prompt}
    messages.append(user_role)

    modelname = "llama3.2:latest"

    response = ollama.chat(
        model=modelname,
        messages=messages
    )

    assistant_response = response.message.content
    print(f"Assistant: {assistant_response}")

    assistant_role = {
        "role": "assistant",
        "content": assistant_response
    }

    messages.append(assistant_role)
