from flask import Blueprint, jsonify, g
from time import time
from services.ai_service import AIService

recommend_bp = Blueprint("recommend", __name__)
ai_service = AIService()

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    payload = getattr(g, "cleaned_json", {})
    text = payload.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    result = ai_service.recommend(text)
    result["generated_at"] = time()

    return jsonify(result), 200
