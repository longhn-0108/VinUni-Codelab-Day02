"""Shared SDK transport and strict JSON parsing; no key needed on import."""
import json
import os

DRAFT_TAG = "[DRAFT_ONLY]"


class BoundaryError(ValueError):
    """Reject output and refer the case to a human operator."""


def encode_draft(payload: dict) -> str:
    return DRAFT_TAG + "\n" + json.dumps(payload, ensure_ascii=False, allow_nan=False)


def decode_draft(text: str) -> dict:
    if not isinstance(text, str) or not text.startswith(DRAFT_TAG + "\n"):
        raise BoundaryError("Response must begin with draft tag and newline")

    def no_duplicates(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise BoundaryError("Duplicate JSON field")
            result[key] = value
        return result

    def invalid_constant(value):
        raise BoundaryError("Non-finite JSON number")

    try:
        payload = json.loads(text[len(DRAFT_TAG):].strip(),
            object_pairs_hook=no_duplicates, parse_constant=invalid_constant)
    except (ValueError, TypeError) as exc:
        raise BoundaryError("Invalid response JSON") from exc
    if not isinstance(payload, dict):
        raise BoundaryError("Expected a JSON object")
    return payload


def generate_json(*, system_prompt, user_input, schema, model) -> dict:
    key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
    if not key:
        raise RuntimeError("Set GEMINI_API_KEY or GOOGLE_API_KEY before --live")
    try:
        from google import genai
        from google.genai import types
    except ImportError as exc:
        raise RuntimeError("Install requirements.txt for --live") from exc
    with genai.Client(api_key=key, http_options=types.HttpOptions(
        timeout=20_000, retry_options=types.HttpRetryOptions(attempts=1))) as client:
        response = client.models.generate_content(model=model, contents=user_input,
            config=types.GenerateContentConfig(system_instruction=system_prompt,
                temperature=0, response_mime_type="application/json",
                response_json_schema=schema, max_output_tokens=1024))
    if not response.text or not response.text.strip():
        raise BoundaryError("Empty or blocked model response")
    return decode_draft(DRAFT_TAG + "\n" + response.text)
