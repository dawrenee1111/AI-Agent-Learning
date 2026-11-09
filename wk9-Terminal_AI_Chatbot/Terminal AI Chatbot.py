import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history=[
    {"role":"system", "content":"You are a helpful assistant."}
    ]

print("Chatbot initialized! Type 'quit' to exit.\n")

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    conversation_history.append({"role":"user", "content":user_input})
    try:
        chat_completion = client.chat.completions.create(model="openai/gpt-oss-20b", messages=conversation_history)
        ai_response = chat_completion.choices[0].message.content
        conversation_history.append({"role":"assistant", "content":ai_response})
        print(f"AI: {ai_response}\n")
    except Exception as e:
        print(f"\nAn error has occurred: {e}")
        conversation_history.pop()
