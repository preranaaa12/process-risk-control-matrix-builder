import logging
import os
from time import time

from dotenv import load_dotenv
from flask import Flask, jsonify, g, request
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address
from routes.describe import describe_bp

from utils.security import contains_prompt_injection, sanitize_payload

load_dotenv()

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s [%(name)s] %(message)s"
)

logger = logging.getLogger(__name__)

start_time = time()


def create_app():
    app = Flask(__name__)

    limiter = Limiter(
        key_func=get_remote_address,
        default_limits=["30 per minute"]
    )
    limiter.init_app(app)

    @app.before_request
    def before_request():
        if request.is_json:
            raw_payload = request.get_json(silent=True) or {}
            cleaned_payload = sanitize_payload(raw_payload)

            payload_text = str(cleaned_payload)
            if contains_prompt_injection(payload_text):
                logger.warning("Prompt injection attempt blocked from IP=%s", request.remote_addr)
                return jsonify({
                    "error": "Suspicious input detected",
                    "message": "Prompt injection patterns detected"
                }), 400

            g.cleaned_json = cleaned_payload

    @app.get("/health")
    def health():
        uptime_seconds = round(time() - start_time, 2)
        return jsonify({
            "status": "ok",
            "service": "ai-service",
            "uptime_seconds": uptime_seconds
        }), 200

    @app.post("/test-sanitize")
    def test_sanitize():
        payload = getattr(g, "cleaned_json", {})
        return jsonify({
            "sanitized": payload
        }), 200

    return app


app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", "5000"))
    app.run(host="0.0.0.0", port=port, debug=True)
