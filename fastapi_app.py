import os
from fastapi import FastAPI, HTTPException
from openai import OpenAI
from dotenv import load_dotenv

from ai_token_monitor import TokenMonitor, ChatManager
from ai_token_monitor.utils import normalize_response, extract_reply

load_dotenv()  # Reads .env file

app = FastAPI(title="AI Token Monitor Demo")

monitor = TokenMonitor()
chat_manager = ChatManager()

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ["OPENROUTER_API_KEY"],  # Set in .env, never hardcode
)

MODEL = "openai/gpt-4o-mini"


@app.post("/chat/start")
def start_chat(user_id: str):
    """Create a new chat session for a user."""
    chat_id = chat_manager.create_chat(user_id)
    return {"chat_id": chat_id}


@app.post("/chat/message")
def chat(chat_id: str, message: str):
    """Send a message and get a tracked response."""
    try:
        chat_manager.add_message(chat_id, "user", message)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Chat ID '{chat_id}' not found.")

    # Call the LLM with full message history
    raw_response = client.chat.completions.create(
        model=MODEL,
        messages=chat_manager.get_messages(chat_id),
    )

    # Normalize Pydantic → dict (fixes the original bug)
    data = normalize_response(raw_response)

    # Safely extract the reply text
    answer = extract_reply(data)

    # Store assistant reply
    chat_manager.add_message(chat_id, "assistant", answer)

    # Track token usage and cost
    usage_log = monitor.track(
        data,
        model=MODEL,
        chat_manager=chat_manager,
        chat_id=chat_id,
    )

    return {
        "answer": answer,
        "usage": usage_log,
        "chat_summary": chat_manager.summary(chat_id),
        "global_summary": monitor.summary(),
    }


@app.get("/monitor/summary")
def global_summary():
    """Get total tokens and cost across all requests."""
    return monitor.summary()


@app.get("/chat/{chat_id}/summary")
def chat_summary(chat_id: str):
    """Get usage summary for a specific chat session."""
    try:
        return chat_manager.summary(chat_id)
    except KeyError:
        raise HTTPException(status_code=404, detail=f"Chat ID '{chat_id}' not found.")
