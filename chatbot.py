from openai import OpenAI

client = OpenAI(
    # put your api key here
    api_key="MY_API"
)

print("🤖 Terminal Chatbot Started")
print("Type 'exit' to quit\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Bye 👋")
        break

    response = client.responses.create(
        model="gpt-4.1-mini",
        input=user_input
    )

    print("Bot:", response.output_text)
