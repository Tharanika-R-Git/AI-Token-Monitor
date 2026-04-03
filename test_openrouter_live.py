import os
from openai import OpenAI
from ai_token_monitor import TokenMonitor, ChatManager, InMemoryStorage
from dotenv import load_dotenv

load_dotenv()

def main():
    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("Missing OPENROUTER_API_KEY in environment or .env file")

    # OpenRouter uses an OpenAI-compatible API with base_url set to OpenRouter
    client = OpenAI(
        api_key=api_key,
        base_url="https://openrouter.ai/api/v1",
    )

    monitor = TokenMonitor()
    chat_manager = ChatManager()
    storage = InMemoryStorage()

    chat_id = chat_manager.create_chat("user_123")

    user_prompt = "Explain token monitoring in 5 simple bullet points."
    chat_manager.add_message(chat_id, "user", user_prompt)

    model_name = "openrouter/free"  
    # You can also try:
    # "deepseek/deepseek-r1:free"
    # "meta-llama/llama-3.3-70b-instruct:free"
    # "openai/gpt-5.4"   <- paid model if your account has credits

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {
                "role": "user",
                "content": user_prompt
            }
        ],
        extra_headers={
            "HTTP-Referer": "http://localhost:8000",
            "X-Title": "AI Token Monitor Local Test"
        }
    )

    # extract assistant reply safely from SDK object
    reply = response.choices[0].message.content if response.choices else ""
    chat_manager.add_message(chat_id, "assistant", reply or "")

    # track token usage using your package
    log = monitor.track(
        response=response,
        model=model_name,
        chat_manager=chat_manager,
        chat_id=chat_id
    )

    storage.save(log)

    print("\n=== ASSISTANT REPLY ===")
    print(reply)

    print("\n=== TRACK LOG ===")
    print(log)

    print("\n=== MONITOR SUMMARY ===")
    print(monitor.summary())

    print("\n=== CHAT SUMMARY ===")
    print(chat_manager.summary(chat_id))

    print("\n=== SAVED RECORDS ===")
    print(storage.get_all())

if __name__ == "__main__":
    main()