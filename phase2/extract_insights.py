import sys
import os
import json
import time
import requests
from datetime import datetime

GITHUB_API = "https://api.github.com/search/repositories"
QUERY_TERMS = [
    "uidai",
    "uidai hackathon",
    "aadhaar"
]

START_DATE = "2026-01-05"
MAX_REPOS = 220  # safety cap

def search_repositories():
    repos = {}
    for term in QUERY_TERMS:
        query = f"{term} created:>={START_DATE}"
        params = {
            "q": query,
            "sort": "updated",
            "order": "desc",
            "per_page": 100
        }

        try:
            resp = requests.get(GITHUB_API, params=params, timeout=30)
            if resp.status_code != 200:
                continue

            for item in resp.json().get("items", []):
                repos[item["html_url"]] = True

            if len(repos) >= MAX_REPOS:
                break

        except Exception:
            continue

    return list(repos.keys())


