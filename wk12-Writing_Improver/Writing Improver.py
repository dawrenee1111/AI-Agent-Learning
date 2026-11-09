import os
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history=[
    {
        "role":"system", 
        "content": (
            "You are an expert Writing Improver. Follow these steps strictly:\n"
            "1. When the user pastes text, DO NOT rewrite it yet. Instead, acknowledge you received it "
            "and list the available styles (Simple, Formal, Persuasive, Creative) asking which one they want.\n"
            "2. Once the user replies with their chosen style, rewrite their original text "
            "into that specific style. Provide only the final polished text so they can copy-paste it easily.")}]
print("Writing Improver ready! Paste your text below. Type 'quit' to exit.\n")
while True:
    user_input = input("You: ")
    if user_input.lower() in ['quit', 'exit']: 
        print("Goodbye!")
        break
    conversation_history.append({"role": "user", "content": user_input})
    try:
        chat_completion = client.chat.completions.create(model="openai/gpt-oss-20b", messages=conversation_history)
        ai_response = chat_completion.choices[0].message.content
        print(f"\nAI: {ai_response}\n")
        conversation_history.append({"role": "assistant", "content": ai_response})
    except Exception as e: 
        print(f"\nAn error has occurred: {e}")
        conversation_history.pop()