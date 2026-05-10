import json
import re
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

    def _parse_json(self, response: str, default: any):
        try:
            # Strip markdown code blocks if present
            cleaned = re.sub(r"```(?:json)?", "", response).strip()
            return json.loads(cleaned)
        except json.JSONDecodeError:
            return default

    def recommend(self, text: str):
        system_prompt = "You are a risk mitigation assistant. Provide 3 recommendations as a JSON array. Each object must have action_type, description, priority. Output ONLY raw JSON, no markdown."
        user_prompt = f"Provide 3 recommendations for the following process/risk:\n{text}"
        response = self.client.chat_completion(system_prompt, user_prompt)
        
        if not response:
            return {"success": False, "is_fallback": True, "data": []}
            
        parsed_data = self._parse_json(response, [])
        return {"success": True, "is_fallback": False, "data": parsed_data}

    def generate_report(self, text: str):
        system_prompt = "You are an audit assistant. Output a structured JSON with title, summary, overview, key_items, recommendations. Output ONLY raw JSON, no markdown."
        user_prompt = f"Generate an executive report for the following context:\n{text}"
        response = self.client.chat_completion(system_prompt, user_prompt)
        
        if not response:
            return {"success": False, "is_fallback": True, "data": {}}
            
        parsed_data = self._parse_json(response, {})
        return {"success": True, "is_fallback": False, "data": parsed_data}