
# GitHub Repository Insights Scanner

A lightweight, local-first tool that scans GitHub repositories and extracts
the **key insights or findings claimed by project authors** from their
documentation (e.g. README files).

The tool is designed for exploratory analysis, competitive intelligence,
and rapid understanding of large sets of open-source projects.

---

## What this tool does

- Searches GitHub for repositories matching a keyword
- Fetches project documentation (README)
- Uses a local LLM (via Ollama) to extract:
  - Insights
  - Findings
  - Key conclusions claimed by authors
- Prints concise bullet-point summaries per repository

This tool **does not judge or rank projects**.  
It focuses purely on *what authors claim they discovered*.

---

## Why this exists

When analyzing many repositories (e.g. hackathons, research repos, open-source
projects), manually reading each README is slow and error-prone.

This tool automates the first pass:
- What insights are common?
- What themes appear repeatedly?
- What ideas stand out?

---

## Requirements

- Python 3.10+
- Ollama installed and running
- A local LLM (e.g. `phi`, `qwen`, `gemma`)

---

## Installation

```bash
pip install -r requirements.txt

