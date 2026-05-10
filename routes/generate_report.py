from flask import Blueprint, jsonify, g
from time import time
from services.ai_service import AIService

generate_report_bp = Blueprint("generate_report", __name__)
ai_service = AIService()

@generate_report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    payload = getattr(g, "cleaned_json", {})
    text = payload.get("text")

    if not text:
        return jsonify({"error": "text is required"}), 400

    result = ai_service.generate_report(text)
    result["generated_at"] = time()

    return jsonify(result), 200
