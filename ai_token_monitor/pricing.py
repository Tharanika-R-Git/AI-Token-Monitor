# =============================================================================
# OpenRouter Model Pricing — Updated April 2026
# Source: https://openrouter.ai/models + https://openrouter.ai/models?q=free
#
# All prices are in USD per 1,000 tokens (divide per-million rates by 1000).
# Free models use ":free" suffix as per OpenRouter convention.
# A value of 0.0 means the model is completely free to use.
#
# Rate limits for free models:
#   - 20 requests/minute
#   - 200 requests/day
# =============================================================================

MODEL_PRICING = {

    # =========================================================================
    # FREE MODELS (input: 0.0, output: 0.0)
    # Use the ":free" suffix exactly as OpenRouter requires
    # =========================================================================

    # Xiaomi MiMo — #1 open-source on SWE-bench, 309B MoE, hybrid thinking
    "xiaomi/mimo-v2-flash:free":                 {"input": 0.0,      "output": 0.0},

    # Mistral Devstral 2 — 123B agentic coding model, modified MIT license
    "mistralai/devstral-2-2512:free":            {"input": 0.0,      "output": 0.0},

    # NVIDIA Nemotron 3 Nano — 30B MoE, fully open weights, agentic AI
    "nvidia/llama-3.3-nemotron-nano-3b-v1:free": {"input": 0.0,      "output": 0.0},

    # DeepSeek V3.1 Nex-N1 — agent autonomy and tool use, 131K context
    "deepseek/deepseek-v3-nex-n1:free":          {"input": 0.0,      "output": 0.0},

    # StepFun Step 3.5 Flash — 256K context, good general performance
    "stepfun/step-3-5-flash:free":               {"input": 0.0,      "output": 0.0},

    # Upstage Solar Pro 3 — strong multilingual, 128K context
    "upstage/solar-pro-3:free":                  {"input": 0.0,      "output": 0.0},

    # DeepSeek R1 — strong reasoning, popular free model
    "deepseek/deepseek-r1:free":                 {"input": 0.0,      "output": 0.0},

    # DeepSeek V3 — general purpose free model
    "deepseek/deepseek-v3:free":                 {"input": 0.0,      "output": 0.0},

    # Meta Llama 3.3 70B — strong free model for general tasks
    "meta-llama/llama-3.3-70b-instruct:free":    {"input": 0.0,      "output": 0.0},

    # Google Gemma 3 27B — Google's open model
    "google/gemma-3-27b-it:free":                {"input": 0.0,      "output": 0.0},

    # Qwen 2.5 72B free tier
    "qwen/qwen-2.5-72b-instruct:free":           {"input": 0.0,      "output": 0.0},

    # OpenRouter's own free router model
    "openrouter/free":                           {"input": 0.0,      "output": 0.0},


    # =========================================================================
    # PAID MODELS — ANTHROPIC (Claude)
    # =========================================================================

    # Claude Opus 4.6 — maximum intelligence, 1M context, agentic tasks
    "anthropic/claude-opus-4-6":                {"input": 0.005,    "output": 0.025},

    # Claude Sonnet 4.6 — mid-range workhorse, 1M context, best value Anthropic
    "anthropic/claude-sonnet-4-6":              {"input": 0.003,    "output": 0.015},

    # Claude Haiku 4.5 — fastest Anthropic model, 200K context
    "anthropic/claude-haiku-4-5":               {"input": 0.001,    "output": 0.005},

    # Claude 3.5 Sonnet (legacy)
    "anthropic/claude-3.5-sonnet":              {"input": 0.003,    "output": 0.015},

    # Claude 3 Haiku (legacy, cheapest Claude)
    "anthropic/claude-3-haiku":                 {"input": 0.00025,  "output": 0.00125},


    # =========================================================================
    # PAID MODELS — OPENAI
    # =========================================================================

    # GPT-5.4 — latest frontier, 1M context, computer use, 57.7% SWE-Bench
    "openai/gpt-5.4":                           {"input": 0.0025,   "output": 0.015},

    # GPT-5.4 Pro — maximum reasoning, mandatory thinking, 1M context
    "openai/gpt-5.4-pro":                       {"input": 0.030,    "output": 0.180},

    # GPT-4o — strong multimodal model
    "openai/gpt-4o":                            {"input": 0.0025,   "output": 0.010},

    # GPT-4o Mini — budget OpenAI option
    "openai/gpt-4o-mini":                       {"input": 0.00015,  "output": 0.0006},

    # o3 — reasoning-focused model
    "openai/o3":                                {"input": 0.010,    "output": 0.040},

    # o4-mini — affordable reasoning model
    "openai/o4-mini":                           {"input": 0.0011,   "output": 0.0044},


    # =========================================================================
    # PAID MODELS — GOOGLE (Gemini)
    # =========================================================================

    # Gemini 3.1 Pro Preview — strongest Google reasoning, 1M context
    "google/gemini-3.1-pro-preview":            {"input": 0.002,    "output": 0.012},

    # Gemini 3.1 Flash Lite — fastest Google model, 1M context, budget king
    "google/gemini-3.1-flash-lite":             {"input": 0.00025,  "output": 0.0015},

    # Gemini 3 Flash — high-speed thinking, 1M context
    "google/gemini-3-flash":                    {"input": 0.0005,   "output": 0.003},

    # Gemini 2.5 Pro — previous generation, still strong
    "google/gemini-2.5-pro-preview":            {"input": 0.00125,  "output": 0.010},

    # Gemini 2.5 Flash — fast and affordable
    "google/gemini-2.5-flash-preview":          {"input": 0.00015,  "output": 0.0006},


    # =========================================================================
    # PAID MODELS — DEEPSEEK
    # =========================================================================

    # DeepSeek V3.2 — ~90% of GPT-5.4 performance at 1/50th the cost
    "deepseek/deepseek-v3-2":                   {"input": 0.00025,  "output": 0.00038},

    # DeepSeek R1 (paid) — stronger reasoning, no rate limits
    "deepseek/deepseek-r1":                     {"input": 0.00055,  "output": 0.00219},


    # =========================================================================
    # PAID MODELS — xAI (Grok)
    # =========================================================================

    # Grok 4.1 Fast — 2M token context, fastest frontier model
    "x-ai/grok-4-1-fast":                       {"input": 0.0002,   "output": 0.0005},

    # Grok 3 Beta — strong reasoning and coding
    "x-ai/grok-3-beta":                         {"input": 0.003,    "output": 0.015},


    # =========================================================================
    # PAID MODELS — MISTRAL
    # =========================================================================

    # Devstral 2 (paid) — 123B agentic coder, no rate limits
    "mistralai/devstral-2-2512":                {"input": 0.00005,  "output": 0.00022},

    # Mistral Large
    "mistralai/mistral-large-2411":             {"input": 0.002,    "output": 0.006},

    # Mixtral 8x7B
    "mistralai/mixtral-8x7b-instruct":          {"input": 0.00024,  "output": 0.00024},

    # Mistral 7B
    "mistralai/mistral-7b-instruct":            {"input": 0.00007,  "output": 0.00007},


    # =========================================================================
    # PAID MODELS — META (Llama)
    # =========================================================================

    # Llama 3.3 70B (paid) — no rate limits
    "meta-llama/llama-3.3-70b-instruct":        {"input": 0.00012,  "output": 0.0003},

    # Llama 3.1 405B — largest Meta model
    "meta-llama/llama-3.1-405b-instruct":       {"input": 0.003,    "output": 0.003},


    # =========================================================================
    # PAID MODELS — QWEN (Alibaba)
    # =========================================================================

    # Qwen3.5 Plus — 1M context, excellent reasoning, ultra-low cost
    "qwen/qwen3.5-plus":                        {"input": 0.0004,   "output": 0.002},

    # Qwen3 Coder Next — coding specialist, budget agents
    "qwen/qwen3-coder-next":                    {"input": 0.00012,  "output": 0.00075},

    # Qwen 2.5 72B (paid)
    "qwen/qwen-2.5-72b-instruct":               {"input": 0.00013,  "output": 0.0004},


    # =========================================================================
    # PAID MODELS — BYTEDANCE (Seed)
    # =========================================================================

    # Seed 1.6 — multimodal, adaptive deep thinking, video understanding
    "bytedance/seed-1.6":                       {"input": 0.00025,  "output": 0.002},

    # Seed 1.6 Flash — ultra-fast multimodal
    "bytedance/seed-1.6-flash":                 {"input": 0.00007,  "output": 0.0003},


    # =========================================================================
    # PAID MODELS — MINIMAX
    # =========================================================================

    # MiniMax M2.1 — 72.5% SWE-Bench Multilingual, best value coding
    "minimax/minimax-m2.1":                     {"input": 0.00028,  "output": 0.001},


    # =========================================================================
    # PAID MODELS — MOONSHOT (Kimi)
    # =========================================================================

    # Kimi K2.5 — agent swarm, 100 sub-agents, 1500 parallel tool calls
    "moonshot/kimi-k2.5":                       {"input": 0.0005,   "output": 0.002},


    # =========================================================================
    # PAID MODELS — Z.AI (GLM)
    # =========================================================================

    # GLM 5 — upgraded reasoning and programming
    "z-ai/glm-5":                               {"input": 0.00095,  "output": 0.003},

    # GLM 4.7 — enhanced programming, stable multi-step reasoning
    "z-ai/glm-4.7":                             {"input": 0.0004,   "output": 0.002},


    # =========================================================================
    # PAID MODELS — KWAI (Kat Coder)
    # =========================================================================

    # Kat Coder Pro — 73.4% SWE-Bench, ultra-low cost agentic coding
    "kwai/kat-coder-pro":                       {"input": 0.00021,  "output": 0.00083},


    # =========================================================================
    # PAID MODELS — ALLENAI (OLMo)
    # =========================================================================

    # OLMo 3.1 32B Think — fully open-source reasoning, Apache 2.0
    "allenai/olmo-3.1-32b-think":               {"input": 0.00015,  "output": 0.0005},

}


# =============================================================================
# Helper functions
# =============================================================================

def get_cost(model: str, prompt_tokens: int, completion_tokens: int) -> float:
    """
    Calculate cost for a given model and token counts.

    Args:
        model:             OpenRouter model ID (e.g. "openai/gpt-4o-mini")
        prompt_tokens:     Number of input/prompt tokens used
        completion_tokens: Number of output/completion tokens used

    Returns:
        Cost in USD as a float. Returns 0.0 for unknown models.
    """
    pricing = MODEL_PRICING.get(model)

    if not pricing:
        print(f"[pricing] WARNING: Unknown model '{model}' — cost defaults to $0.0. "
              f"Check MODEL_PRICING or visit https://openrouter.ai/models")
        return 0.0

    input_cost  = (prompt_tokens     / 1000) * pricing["input"]
    output_cost = (completion_tokens / 1000) * pricing["output"]

    return input_cost + output_cost


def get_free_models() -> list:
    """Return a list of all free model IDs (cost = $0.0)."""
    return [
        model for model, price in MODEL_PRICING.items()
        if price["input"] == 0.0 and price["output"] == 0.0
    ]


def get_paid_models() -> list:
    """Return a list of all paid model IDs."""
    return [
        model for model, price in MODEL_PRICING.items()
        if price["input"] > 0.0 or price["output"] > 0.0
    ]


def get_model_pricing(model: str) -> dict | None:
    """
    Return the raw pricing dict for a model, or None if not found.

    Example:
        get_model_pricing("openai/gpt-4o-mini")
        >> {"input": 0.00015, "output": 0.0006}
    """
    return MODEL_PRICING.get(model)


def estimate_cost(model: str, input_words: int, output_words: int) -> float:
    """
    Rough cost estimate from word counts (1 token ~= 0.75 words).

    Args:
        model:        OpenRouter model ID
        input_words:  Approximate number of words in your prompt
        output_words: Approximate number of words in the expected response

    Returns:
        Estimated cost in USD.
    """
    prompt_tokens     = int(input_words  / 0.75)
    completion_tokens = int(output_words / 0.75)
    return get_cost(model, prompt_tokens, completion_tokens)


def list_supported_models() -> list:
    """Return all model IDs currently in the pricing table."""
    return list(MODEL_PRICING.keys())


def cheapest_models(top_n: int = 5) -> list:
    """
    Return the top N cheapest paid models sorted by output token cost.
    Free models are excluded — use get_free_models() for those.
    """
    paid = {k: v for k, v in MODEL_PRICING.items() if v["output"] > 0}
    sorted_models = sorted(paid.items(), key=lambda x: x[1]["output"])
    return [
        {"model": k, "input_per_1k": v["input"], "output_per_1k": v["output"]}
        for k, v in sorted_models[:top_n]
    ]