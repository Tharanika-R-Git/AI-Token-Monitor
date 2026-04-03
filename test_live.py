import os
from openai import OpenAI
from dotenv import load_dotenv
from ai_token_monitor import TokenMonitor, ChatManager
from ai_token_monitor.utils import normalize_response, extract_reply

# Load environment variables
load_dotenv()

# Initialize OpenAI client with OpenRouter base URL
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# Initialize monitor and chat manager
monitor = TokenMonitor()
chat_manager = ChatManager()

# Create a new chat session
chat_id = chat_manager.create_chat("user_123")

# Add user message
user_message = "Hello! What is the capital of France?"
chat_manager.add_message(chat_id, "user", user_message)
use_model="openrouter/free"
# Call OpenRouter API
response = client.chat.completions.create(
    model=use_model,
    messages=[
        {"role": "user", "content": user_message}
    ]
)

# Normalize and extract response
data = normalize_response(response.model_dump())
answer = extract_reply(data)

# Track tokens
monitor.track(data, model=use_model, chat_manager=chat_manager, chat_id=chat_id)

# Add assistant message to chat
chat_manager.add_message(chat_id, "assistant", answer)

# Print summary
print("Answer:", answer)
print("\nToken Summary:")
print(monitor.summary())
