# SECURITY.md

## Security Review — AI Service

This document captures the main security threats identified for the Flask AI microservice and the controls planned or implemented.

## Scope
Applies to:
- Flask AI service
- Groq API integration
- Input handling for AI endpoints
- Rate limiting and abuse prevention

## Threats Identified

### 1. Prompt Injection
**Risk:** Users may submit malicious instructions intended to override system prompts, leak hidden instructions, or manipulate output.  
**Mitigation:** Input validation, prompt injection keyword detection, strict system prompts, reject suspicious requests with HTTP 400.

### 2. API Abuse / Denial of Service
**Risk:** Attackers may spam endpoints and exhaust free-tier AI quota or degrade service.  
**Mitigation:** `flask-limiter` set to 30 requests per minute per IP, request timeouts, retry limits.

### 3. Secret Exposure
**Risk:** Groq API keys may be committed to source control or exposed in logs.  
**Mitigation:** Store secrets only in `.env`, add `.env` to `.gitignore`, never log API keys, use `.env.example` for reference only.

### 4. Malicious Input / XSS Payloads
**Risk:** Users may submit HTML or script payloads that get stored, logged, or reflected into responses.  
**Mitigation:** Strip HTML tags, sanitize inputs before prompt construction, validate allowed input length and format.

### 5. Unhandled Third-Party Failures
**Risk:** Groq outages, rate limits, or malformed responses could break the service and return HTTP 500.  
**Mitigation:** Wrap all Groq calls in try/except, implement 3 retries with backoff, log safely, return fallback responses instead of crashing.

## Residual Risks
- Prompt injection detection is heuristic and may not catch every attack.
- Free-tier provider outages may still reduce AI quality even with fallback logic.
- Rate limiting by IP may be less effective behind shared NAT/proxy environments.

## Next Actions
- Add request sanitisation middleware
- Add prompt injection detection
- Add test coverage for rejected malicious inputs
- Add fallback JSON responses on model failure
