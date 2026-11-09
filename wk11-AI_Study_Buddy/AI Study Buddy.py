import os
from groq import Groq
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
conversation_history=[
    {"role":"system", "content": ("You are an AI Study Buddy. Follow this exact process: 1. When the user gives a topic: Explain it simply in plain language, then give exactly 5 quiz questions. Stop and wait for the user's answers. 2. When the user gives answers: Check each answer, say if it is correct or incorrect, give a short explanation, and then wait for a new topic.")}]    
print("Study Buddy ready! Enter your topic below. Type 'quit' to exit.\n")
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