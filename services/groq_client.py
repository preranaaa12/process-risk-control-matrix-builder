import logging
import os
import time
from typing import Optional

import requests
from dotenv import load_dotenv

load_dotenv()

logger = logging.getLogger(__name__)


class GroqClient:
    def __init__(self):
        self.api_key = os.getenv("GROQ_API_KEY")
        self.model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
        self.base_url = "[api.groq.com](https://api.groq.com/openai/v1/chat/completions)"
        self.timeout = 20

        if not self.api_key:
            raise ValueError("GROQ_API_KEY is missing from environment")

    def chat_completion(
        self,
        system_prompt: str,
        user_prompt: str,
        temperature: float = 0.3,
        max_tokens: int = 700
    ) -> Optional[str]:
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": self.model,
            "temperature": temperature,
            "max_tokens": max_tokens,
            "messages": [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ]
        }

        max_retries = 3
        backoffs = [1, 2, 4]

        for attempt in range(max_retries):
            try:
                response = requests.post(
                    self.base_url,
                    headers=headers,
                    json=payload,
                    timeout=self.timeout
                )

                if response.status_code >= 400:
                    logger.warning(
                        "Groq API returned error status=%s body=%s",
                        response.status_code,
                        response.text
                    )

                response.raise_for_status()

                data = response.json()

                if "choices" not in data or not data["choices"]:
                    logger.error("Groq response missing choices: %s", data)
                    return None

                message = data["choices"][0].get("message", {})
                content = message.get("content")

                if not content:
                    logger.error("Groq response missing message content: %s", data)
                    return None

                return content.strip()

            except requests.exceptions.RequestException as exc:
                logger.exception(
                    "Groq call failed on attempt %s/%s",
                    attempt + 1,
                    max_retries
                )
                if attempt < max_retries - 1:
                    time.sleep(backoffs[attempt])
                else:
                    logger.error("Groq call failed after all retries: %s", exc)

            except (KeyError, ValueError, TypeError) as exc:
                logger.exception("Failed parsing Groq response: %s", exc)
                return None

        return None
