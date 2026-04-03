# AI Token Monitor 🚀

Track token usage and cost for OpenRouter, Groq, and OpenAI — with FastAPI integration.

## Features
- ✅ Token tracking per request and per chat session
- ✅ Cost estimation (real model pricing)
- ✅ Multi-turn chat session management
- ✅ FastAPI integration with middleware
- ✅ Production logging

## Install

```bash
pip install ai-token-monitor
```

## Quick Start

```python
from ai_token_monitor import TokenMonitor, ChatManager
from ai_token_monitor.utils import normalize_response, extract_reply

monitor = TokenMonitor()
chat_manager = ChatManager()

chat_id = chat_manager.create_chat("user_123")
chat_manager.add_message(chat_id, "user", "Hello!")

# After getting response from OpenAI/OpenRouter:
data = normalize_response(raw_response)
answer = extract_reply(data)
monitor.track(data, model="openai/gpt-4o-mini", chat_manager=chat_manager, chat_id=chat_id)

print(monitor.summary())
```

## Environment Variables

Copy `.env.example` to `.env` and set:

```
OPENROUTER_API_KEY=your_key_here
```

## Run the FastAPI Example

```bash
uvicorn examples.fastapi_app:app --reload
```

## Supported Models

- `openrouter/free`
- `deepseek/deepseek-r1:free`
- `deepseek/deepseek-v3:free`
- `meta-llama/llama-3.3-70b-instruct:free`
- `qwen/qwen-2.5-72b-instruct:free`
- `google/gemma-3-27b-it:free`
- `mistralai/devstral-2-2512:free`
- `xiaomi/mimo-v2-flash:free`
- `nvidia/llama-3.3-nemotron-nano-3b-v1:free`
- `stepfun/step-3-5-flash:free`
- `upstage/solar-pro-3:free`

---

### 💰 Paid Models

#### 🔹 OpenAI
- `openai/gpt-5.4`
- `openai/gpt-5.4-pro`
- `openai/gpt-4o`
- `openai/gpt-4o-mini`
- `openai/o3`
- `openai/o4-mini`

#### 🔹 Anthropic (Claude)
- `anthropic/claude-opus-4-6`
- `anthropic/claude-sonnet-4-6`
- `anthropic/claude-haiku-4-5`

#### 🔹 Google Gemini
- `google/gemini-3.1-pro-preview`
- `google/gemini-3.1-flash-lite`
- `google/gemini-3-flash`

#### 🔹 DeepSeek
- `deepseek/deepseek-v3-2`
- `deepseek/deepseek-r1`

#### 🔹 Mistral
- `mistralai/devstral-2-2512`
- `mistralai/mistral-large-2411`
- `mistralai/mixtral-8x7b-instruct`

#### 🔹 Meta (Llama)
- `meta-llama/llama-3.3-70b-instruct`
- `meta-llama/llama-3.1-405b-instruct`

#### 🔹 Qwen (Alibaba)
- `qwen/qwen3.5-plus`
- `qwen/qwen3-coder-next`

#### 🔹 xAI (Grok)
- `x-ai/grok-4-1-fast`
- `x-ai/grok-3-beta`

#### 🔹 Others
- `bytedance/seed-1.6`
- `minimax/minimax-m2.1`
- `moonshot/kimi-k2.5`
- `z-ai/glm-5`
- `kwai/kat-coder-pro`
- `allenai/olmo-3.1-32b-think`
## License

MIT
