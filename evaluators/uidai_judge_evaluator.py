def evaluate_submission(all_text, llm):
    prompt = open("prompts/uidai_judge_prompt.txt").read()
    full_prompt = prompt + "\n\nSUBMISSION CONTENT:\n" + all_text
    return llm(full_prompt)
