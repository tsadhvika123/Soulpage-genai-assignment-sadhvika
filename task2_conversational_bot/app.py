from langchain_community.chat_models import ChatOllama
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

def main():
    # Connect to Phi via Ollama
    llm = ChatOllama(
        model="phi",
        temperature=0
    )

    # Conversation memory
    memory = ConversationBufferMemory(
        return_messages=True
    )

    # Conversation chain
    conversation = ConversationChain(
        llm=llm,
        memory=memory,
        verbose=True
    )

    print("🤖 Conversational Knowledge Bot (type 'exit' to quit)\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Bot: Goodbye! 👋")
            break

        response = conversation.predict(input=user_input)
        print(f"Bot: {response}\n")


if __name__ == "__main__":
    main()
