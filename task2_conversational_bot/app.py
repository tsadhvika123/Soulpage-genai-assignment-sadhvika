from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory
from langchain.chat_models import ChatOpenAI
from langchain.utilities import WikipediaAPIWrapper

llm = ChatOpenAI(temperature=0)
memory = ConversationBufferMemory()

wiki = WikipediaAPIWrapper()

conversation = ConversationChain(
    llm=llm,
    memory=memory,
    verbose=True
)

def start_chat():
    print("🤖 Conversational Knowledge Bot")
    print("Type 'exit' to quit\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() == "exit":
            break

        wiki_info = wiki.run(user_input)

        response = conversation.predict(
            input=f"{user_input}\n\nReference Information:\n{wiki_info}"
        )

        print("Bot:", response)
        print()

if __name__ == "__main__":
    start_chat()