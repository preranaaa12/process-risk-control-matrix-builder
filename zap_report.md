# OWASP ZAP Scan Report (Day 7)

## Scan Details
- **Target:** Flask AI Service (http://localhost:5000)
- **Scan Type:** Active Scan
- **Authentication:** None

## Findings

### Critical
- **None detected.**

### High
- **None detected.**

### Medium
1. **Missing Anti-clickjacking Header (X-Frame-Options)**
   - *Description:* The response does not include the X-Frame-Options header.
   - *Plan:* Implement `flask-talisman` or manually set `X-Frame-Options: DENY` in Flask `after_request`.

2. **X-Content-Type-Options Header Missing**
   - *Description:* The response does not prevent MIME-sniffing.
   - *Plan:* Add `X-Content-Type-Options: nosniff` header.

3. **Content Security Policy (CSP) Header Not Set**
   - *Description:* CSP is not configured, which could allow XSS (though currently mitigated by input sanitization).
   - *Plan:* Add basic CSP header restricting sources to `self`.

### Low / Informational
- **Server Leaks Version Information**
   - *Description:* `Server: Werkzeug/x.x.x Python/x.x.x` is returned.
   - *Plan:* Configure production server (e.g., Gunicorn) to suppress server signatures.

## Fix Strategy (Day 8 Plan)
We will add a Flask `@app.after_request` hook to inject the missing security headers. This will resolve all Medium findings.
