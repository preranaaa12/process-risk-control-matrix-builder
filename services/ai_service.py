from services.groq_client import GroqClient


class AIService:

    def __init__(self):
        self.client = GroqClient()

    def describe(self, text: str):
        system_prompt = "You are a risk analysis assistant."

        user_prompt = f"""
        Describe the following process risk clearly and concisely:

        {text}
        """

        response = self.client.chat_completion(system_prompt, user_prompt)

        if not response:
            return {
                "success": False,
                "is_fallback": True,
                "data": {"text": "AI unavailable"}
            }

        return {
            "success": True,
            "is_fallback": False,
            "data": {"description": response}
        }