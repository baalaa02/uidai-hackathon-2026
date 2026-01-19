import requests
import time

print("=== SCRIPT STARTED ===")

# -----------------------
# CONFIG (HARD LIMITED)
# -----------------------
OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi:latest"

MAX_REPOS = 5
MAX_CHARS = 4000
TIMEOUT = 60

# -----------------------
# STEP 1: GET REPOS
# -----------------------
print("Fetching repositories from GitHub...")

search_url = "https://api.github.com/search/repositories"
params = {
    "q": "uidai",
    "sort": "updated",
    "order": "desc",
    "per_page": MAX_REPOS
}

resp = requests.get(search_url, params=params, timeout=30)
resp.raise_for_status()

repos = [item["full_name"] for item in resp.json()["items"]]
print(f"Found {len(repos)} repos")

# -----------------------
# STEP 2: PROCESS EACH
# -----------------------
for idx, repo in enumerate(repos, 1):
    print(f"\n[{idx}/{len(repos)}] Processing {repo}")

    owner, name = repo.split("/")

    # Fetch README only
    readme_url = f"https://raw.githubusercontent.com/{owner}/{name}/main/README.md"
    r = requests.get(readme_url, timeout=20)

    if r.status_code != 200:
        print("  README not found, skipping")
        continue

    text = r.text[:MAX_CHARS]
    print(f"  README loaded ({len(text)} chars)")

    prompt = f"""
Extract the key data insights or findings explicitly claimed by the authors.

Rules:
- Do NOT judge or critique
- Do NOT add new insights
- Return 3–5 bullet points

CONTENT:
{text}
"""

    print("  Calling Ollama...")
    t0 = time.time()

    ollama_resp = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        },
        timeout=TIMEOUT
    )

    ollama_resp.raise_for_status()
    output = ollama_resp.json()["response"]

    print(f"  Ollama responded in {int(time.time() - t0)}s")
    print("  INSIGHTS:")
    print(output)

print("\n=== SCRIPT FINISHED ===")
