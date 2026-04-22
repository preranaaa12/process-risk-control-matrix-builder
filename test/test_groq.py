import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
GROQ_MODEL = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")

def main():
    if not GROQ_API_KEY:
        raise ValueError("GROQ_API_KEY is missing from environment")

    url = "[api.groq.com](https://api.groq.com/openai/v1/chat/completions)"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": GROQ_MODEL,
        "temperature": 0.3,
        "max_tokens": 200,
        "messages": [
            {"role": "system", "content": "You are a concise assistant."},
            {"role": "user", "content": "Say hello and confirm this Groq API call works."}
        ]
    }

    response = requests.post(url, headers=headers, json=payload, timeout=20)
    print("Status:", response.status_code)
    print("Body:", response.text)

    response.raise_for_status()
    data = response.json()
    content = data["choices"][0]["message"]["content"]
    print("\nParsed content:\n", content)

if __name__ == "__main__":
    main()
