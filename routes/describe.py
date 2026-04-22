from flask import Blueprint, request, jsonify, g
from time import time
from services.ai_service import AIService

describe_bp = Blueprint("describe", __name__)

ai_service = AIService()


@describe_bp.route("/describe", methods=["POST"])
def describe():
    payload = getattr(g, "cleaned_json", {})
    text = payload.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    result = ai_service.describe(text)

    result["generated_at"] = time()

    return jsonify(result), 200