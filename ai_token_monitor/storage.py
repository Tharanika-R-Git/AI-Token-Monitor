import time


class InMemoryStorage:
    """Simple in-memory log store. Replace with DB adapter for production."""

    def __init__(self):
        self.records: list = []

    def save(self, data: dict):
        entry = {**data, "saved_at": time.time()}
        self.records.append(entry)

    def get_all(self) -> list:
        return self.records

    def get_by_model(self, model: str) -> list:
        return [r for r in self.records if r.get("model") == model]

    def clear(self):
        self.records = []
