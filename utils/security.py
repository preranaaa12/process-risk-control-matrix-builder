import re
from typing import Any

import bleach

PROMPT_INJECTION_PATTERNS = [
    r"ignore\s+previous\s+instructions",
    r"ignore\s+all\s+instructions",
    r"disregard\s+previous",
    r"reveal\s+system\s+prompt",
    r"show\s+hidden\s+prompt",
    r"developer\s+message",
    r"system\s+prompt",
    r"bypass\s+safety",
    r"jailbreak",
    r"act\s+as\s+an?\s+unrestricted",
    r"pretend\s+you\s+are",
    r"do\s+not\s+follow\s+prior\s+rules"
]


def sanitize_text(value: str) -> str:
    if value is None:
        return ""
    cleaned = bleach.clean(value, tags=[], attributes={}, strip=True)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    return cleaned


def contains_prompt_injection(text: str) -> bool:
    if not text:
        return False

    lowered = text.lower()
    for pattern in PROMPT_INJECTION_PATTERNS:
        if re.search(pattern, lowered):
            return True
    return False


def sanitize_payload(payload: Any):
    if isinstance(payload, dict):
        return {key: sanitize_payload(value) for key, value in payload.items()}
    if isinstance(payload, list):
        return [sanitize_payload(item) for item in payload]
    if isinstance(payload, str):
        return sanitize_text(payload)
    return payload
