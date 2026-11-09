import os
from groq import Groq

client = Groq(api_key=os.getenv("GROQ_API_KEY"))
system_prompt={
    "role":"system", 
    "content": (
        "You are a smart summarizer. For any text the user provides, "
            "you must strictly return the response in this exact format:\n\n"
            "### 📝 Short Summary\n"
            "[Insert a 2-3 sentence summary here]\n\n"
            "### 🔑 Key Points\n"
            "* [Point 1]\n"
            "* [Point 2]\n"
            "* [Point 3]\n"
            "* [Point 4]\n"
            "* [Point 5]\n\n"
            "### 💡 One-Sentence Version\n"
            "[Insert a single, high-impact sentence summarizing the core takeaway]"
    )
}

print("Smart Summarizer ready! Paste your text below. Type 'quit' to exit.\n")

while True:
    user_input = input("You (paste text): ")
    if user_input.lower() in ['quit', 'exit']:
        print("Goodbye!")
        break
    messages = [
        system_prompt, 
        {"role":"user", "content":user_input}
    ]
    try:
        chat_completion = client.chat.completions.create(model="openai/gpt-oss-20b", messages=messages)
        ai_response = chat_completion.choices[0].message.content
        print(f"\nAI: {ai_response}\n")
    except Exception as e:
        print(f"\nAn error has occurred: {e}")