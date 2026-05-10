# Prompt Tuning Report (Day 6)

## Objective
To test the AI endpoints with 10 real-world risk management inputs, score the accuracy (out of 10), and ensure all outputs are consistently structured and score above 7/10.

## Methodology
10 inputs related to common business processes (e.g., Payroll, Vendor Onboarding, Access Management) were tested against the `/describe`, `/recommend`, and `/generate-report` endpoints.

## Results Summary

| Input ID | Process Context | Score (out of 10) | Notes |
| --- | --- | --- | --- |
| 1 | Payroll Processing | 9 | Excellent JSON structure |
| 2 | Vendor Onboarding | 8 | Recommendations were slightly generic but acceptable |
| 3 | IT Access Provisioning | 10 | Perfect formatting and priority assignment |
| 4 | Asset Disposal | 8 | Good summary, overview could be longer |
| 5 | Financial Reporting | 9 | Strong mitigation strategies |
| 6 | Data Backup | 9 | Clear risk description |
| 7 | Employee Offboarding | 8 | Action types were well-categorized |
| 8 | Cloud Migration | 6 -> 9 | **Failed initial test** (poor JSON formatting). Refined system prompt in `ai_service.py` to enforce strict JSON arrays. Score improved. |
| 9 | Incident Response | 8 | Good context alignment |
| 10 | Contract Review | 9 | Excellent priority ranking |

## Prompt Refinements Made
- **`/recommend` Endpoint:** Updated the prompt to explicitly enforce returning exactly 3 JSON objects in an array.
- **`/generate-report` Endpoint:** Mandated specific JSON keys (`title`, `summary`, `overview`, `key_items`, `recommendations`) to prevent hallucinated data structures.

**Status:** ALL endpoints now consistently scoring 8+ out of 10.
