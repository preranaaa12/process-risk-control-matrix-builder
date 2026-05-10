# Week 2 Quality Review (Day 10)

## Objective
Final review of AI prompts and outputs using 10 *fresh* input scenarios, aiming for an average score >= 4/5.

## Test Batch Results

| ID | Input Scenario | Target Endpoint | Score (1-5) | Notes |
| --- | --- | --- | --- | --- |
| 1 | Server Room Flood Risk | `/describe` | 5 | Very precise description |
| 2 | Phishing Attack | `/recommend` | 5 | Great actionable controls |
| 3 | Insider Threat | `/generate-report` | 4 | Missing minor context in overview |
| 4 | DB Credentials Leak | `/recommend` | 5 | Excellent priority assigned |
| 5 | Ransomware | `/describe` | 5 | Concise and clear |
| 6 | Unpatched Software | `/recommend` | 5 | Good technical suggestions |
| 7 | Regulatory Non-compliance | `/generate-report` | 5 | Structured perfectly |
| 8 | Third-party Data Breach | `/describe` | 4 | slightly too verbose |
| 9 | Loss of Key Personnel | `/recommend` | 5 | Good process-oriented controls |
| 10 | Hardware Failure | `/generate-report` | 5 | Included DR strategies |

## Metrics
- **Average Score:** 4.8 / 5
- **Pass Rate:** 100% (No responses fell into the fallback logic)
- **JSON Stability:** 100% properly formatted JSON strings.

## Conclusion
The AI service logic, prompt templates, and Groq `llama-3.3-70b-versatile` integrations are stable, highly qualitative, and ready for integration testing. No further prompt tuning is required at this stage.
