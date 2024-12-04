from openai_service import call_open_ai
from chromadb_service import retriver
from mongo_service import save_chat, fetch_chat

PROMPT = """The following is a conversation with a Parallel and Distributed Computing Bot. The Bot is helpful, knowledgeable, and friendly. It is designed to answer questions related to Parallel and Distributed Computing.If any irrelevant question is asked say i dont have the answer."""
def my_Bot(question, user_id):
    history = fetch_chat(user_id)
    print(history)
    clean_history = []
    if len(history) > 0:
        for item in history:
            clean_history.append({
                "role": item["role"],
                "content": item["content"]
            })
    print(clean_history)
           
    text = []
    docs = retriver(question)
    for doc in docs:
        text.append(doc.page_content)
    combined_text = " ".join(text)
    messages = [{"role": "system", "content": PROMPT},
                {"role": "system", "content": combined_text},
                
                
                {"role": "user", "content": question}
                ]
    
    messages.extend(clean_history)
    messages.append({"role": "user", "content": question})
    user_chat = {
        "role":"user", "content": question, "user_id": user_id
    }
    save_chat(user_chat)
    response = call_open_ai(messages)
    
    ai_chat = {
        "role":"assistant", "content": response, "user_id": user_id
    }
    save_chat(ai_chat)
    return response

while True:
    question = input("You: Ask me a question ")
    if question == "exit":
        break
    response = my_Bot(question, "xyz123")
    print("Bot:", response)
    
    #langchain loader website > document> different file formats
    # langchain library to build a bot
    