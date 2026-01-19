from evaluators.uidai_judge_evaluator import evaluate_submission
from google import genai
import os

# --------------------------------------------------
# CLIENT SETUP
# --------------------------------------------------

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

# --------------------------------------------------
# FIND ANY MODEL THAT ACTUALLY WORKS
# --------------------------------------------------

def get_working_model():
    models = client.models.list()
    for m in models:
        try:
            # minimal test prompt
            test = client.models.generate_content(
                model=m.name,
                contents="test"
            )
            print(f"Using Gemini model: {m.name}")
            return m.name
        except Exception:
            continue

    raise RuntimeError("No usable Gemini model found on this API key.")

MODEL_NAME = get_working_model()

# --------------------------------------------------
# BASIC JUDGE LLM (NO CONFIG, NO ASSUMPTIONS)
# --------------------------------------------------

def real_llm(prompt: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt
    )
    return response.text

# --------------------------------------------------
# MAIN
# --------------------------------------------------

def main():
    with open("outputs/raw_extracted_content.txt", "r", encoding="utf-8") as f:
        submission_text = f.read()

    evaluation = evaluate_submission(submission_text, real_llm)

    with open("outputs/evaluation_report.md", "w", encoding="utf-8") as f:
        f.write(evaluation)

    with open("outputs/evaluation_report.txt", "w", encoding="utf-8") as f:
        f.write(evaluation)

    print("DONE. Evaluation report generated.")

if __name__ == "__main__":
    main()
