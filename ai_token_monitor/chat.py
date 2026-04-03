import uuid
import time


class ChatManager:
    def __init__(self):
        self.chats: dict = {}

    def create_chat(self, user_id: str) -> str:
        chat_id = str(uuid.uuid4())

        self.chats[chat_id] = {
            "user_id": user_id,
            "messages": [],
            "created_at": time.time(),
            "total_tokens": 0,
            "total_cost": 0.0,
        }

        return chat_id

    def add_message(self, chat_id: str, role: str, content: str):
        chat = self._get_or_raise(chat_id)
        chat["messages"].append({"role": role, "content": content})

    def update_usage(self, chat_id: str, tokens: int, cost: float):
        chat = self._get_or_raise(chat_id)
        chat["total_tokens"] += tokens
        chat["total_cost"] += cost

    def get_chat(self, chat_id: str) -> dict:
        return self._get_or_raise(chat_id)

    def get_messages(self, chat_id: str) -> list:
        """Return only the messages list for use as API context."""
        return self._get_or_raise(chat_id)["messages"]

    def summary(self, chat_id: str) -> dict:
        chat = self._get_or_raise(chat_id)

        return {
            "chat_id": chat_id,
            "user_id": chat["user_id"],
            "messages": len(chat["messages"]),
            "total_tokens": chat["total_tokens"],
            "total_cost": round(chat["total_cost"], 6),
        }

    def delete_chat(self, chat_id: str):
        if chat_id in self.chats:
            del self.chats[chat_id]

    def _get_or_raise(self, chat_id: str) -> dict:
        chat = self.chats.get(chat_id)
        if chat is None:
            raise KeyError(f"Chat ID '{chat_id}' not found.")
        return chat
