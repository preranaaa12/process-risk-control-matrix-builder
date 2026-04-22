from services.groq_client import GroqClient

client = GroqClient()

response = client.chat_completion(
    system_prompt="You are a risk and control matrix assistant.",
    user_prompt="Describe procurement process risk in 3 concise bullet points."
)

print(response)
