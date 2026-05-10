import json
from services.ai_service import AIService

def run_demo():
    print("Initializing AI Service...")
    service = AIService()
    
    test_input = "Employees are sharing their login passwords with each other."
    
    print("\n--- Testing /describe ---")
    describe_result = service.describe(test_input)
    print(json.dumps(describe_result, indent=2))
    
    print("\n--- Testing /recommend ---")
    recommend_result = service.recommend(test_input)
    print(json.dumps(recommend_result, indent=2))
    
    print("\n--- Testing /generate-report ---")
    report_result = service.generate_report(test_input)
    print(json.dumps(report_result, indent=2))

if __name__ == "__main__":
    run_demo()
