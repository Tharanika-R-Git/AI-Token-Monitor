from ai_token_monitor import TokenMonitor, ChatManager, InMemoryStorage

def main():
    # Create objects
    monitor = TokenMonitor()
    chat_manager = ChatManager()
    storage = InMemoryStorage()

    # Create a chat
    chat_id = chat_manager.create_chat("user_123")

    # Add sample messages
    chat_manager.add_message(chat_id, "user", "Hello, tell me about AI token monitoring.")
    chat_manager.add_message(chat_id, "assistant", "Sure, I can help with that.")

    # Fake OpenAI-style response
    fake_response = {
        "usage": {
            "prompt_tokens": 120,
            "completion_tokens": 80,
            "total_tokens": 200
        },
        "choices": [
            {
                "message": {
                    "content": "This is a sample assistant reply."
                }
            }
        ]
    }

    # Use a model that exists in your pricing table
    model_name = "openrouter/free"

    # Track usage
    log = monitor.track(
        response=fake_response,
        model=model_name,
        chat_manager=chat_manager,
        chat_id=chat_id
    )

    # Save log
    storage.save(log)

    # Print results
    print("=== TRACK LOG ===")
    print(log)

    print("\n=== MONITOR SUMMARY ===")
    print(monitor.summary())

    print("\n=== CHAT SUMMARY ===")
    print(chat_manager.summary(chat_id))

    print("\n=== SAVED RECORDS ===")
    print(storage.get_all())


if __name__ == "__main__":
    main()