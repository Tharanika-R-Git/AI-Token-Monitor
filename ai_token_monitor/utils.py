def normalize_response(response) -> dict:
    """
    Normalize an OpenAI SDK response to a plain Python dict.

    The OpenAI Python SDK (v1+) returns Pydantic BaseModel objects.
    This function converts them to dicts so we can use .get() safely.
    Falls back gracefully if already a dict or if model_dump() fails.
    """
    if isinstance(response, dict):
        return response

    # OpenAI SDK v1+ objects expose model_dump()
    if hasattr(response, "model_dump"):
        return response.model_dump()

    # Older SDK used .dict()
    if hasattr(response, "dict"):
        return response.dict()

    raise TypeError(
        f"Cannot normalize response of type {type(response).__name__}. "
        "Expected a dict or Pydantic model."
    )


def extract_reply(data: dict) -> str:
    """
    Extract the assistant's text reply from a normalized response dict.
    Raises ValueError if the structure is unexpected.
    """
    try:
        return data["choices"][0]["message"]["content"]
    except (KeyError, IndexError, TypeError) as e:
        raise ValueError(f"Could not extract reply from response: {e}\nData: {data}")
