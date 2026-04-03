import time
from .pricing import get_cost
from .logger import logger
from .utils import normalize_response


class TokenMonitor:
    def __init__(self):
        self.total_tokens = 0
        self.total_cost = 0.0
        self.logs = []

    def track(self, response, model: str, chat_manager=None, chat_id: str = None):
        """
        Track token usage from an OpenAI-compatible API response.
        Accepts either a Pydantic model (raw SDK response) or a plain dict.
        """
        # Normalize to dict first (fixes Pydantic object issue)
        data = normalize_response(response)

        usage = data.get("usage", {})

        prompt = usage.get("prompt_tokens", 0)
        completion = usage.get("completion_tokens", 0)
        total = usage.get("total_tokens", prompt + completion)

        cost = get_cost(model, prompt, completion)

        self.total_tokens += total
        self.total_cost += cost

        log = {
            "model": model,
            "prompt_tokens": prompt,
            "completion_tokens": completion,
            "total_tokens": total,
            "cost": round(cost, 6),
            "timestamp": time.time(),
        }

        self.logs.append(log)

        if chat_manager and chat_id:
            chat_manager.update_usage(chat_id, total, cost)

        logger.info(f"[{model}] tokens={total}, cost=${cost:.6f}")

        return log

    def summary(self):
        return {
            "total_tokens": self.total_tokens,
            "total_cost": round(self.total_cost, 6),
            "requests": len(self.logs),
        }
