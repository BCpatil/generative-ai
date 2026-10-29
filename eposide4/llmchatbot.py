from langchain_ollama import ChatOllama
from langchain_core.messages import SystemMessage , HumanMessage , AIMessage

llm = ChatOllama (
    model = "llama3.2:latest",
    temperature=0.7
)

messages = [
    SystemMessage(
        content="you are a friendly , helpful assistant."
    )
]

while True :
    user_prompt = input("\nyou:").strip()

    if user_prompt.lower() == "exit":
        print("Assistant : Goodbye ")
        break

    if user_prompt.lower() == "reset":
        messages = [
            SystemMessage(
                content = "you are a friendly , helpful assistant."
            )
        ]
        print("chat history clered.")
        continue
    messages.append(HumanMessage(content=user_prompt))

    try:
        response = llm.invoke(messages)

        assistant_response = response.content
        print(f"\nAssistant:{assistant_response}")

        messages.append(
            AIMessage(content=str(assistant_response))

        )

    except Exception as error :
        messages.pop()
        print(f"Error : {error}")