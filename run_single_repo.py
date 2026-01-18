from collectors.github_collector import get_repo_tree, fetch_file
from config import REPO_URL, SUPPORTED_EXTENSIONS, OUTPUT_MD, OUTPUT_TXT
from parsers.markdown_parser import parse_markdown
from parsers.notebook_parser import parse_notebook

def main():
    owner, repo = REPO_URL.split("/")[-2:]
    tree = get_repo_tree(owner, repo)

    collected_text = []

    for item in tree:
        path = item["path"]
        if any(path.lower().endswith(ext) for ext in SUPPORTED_EXTENSIONS):
            try:
                content = fetch_file(owner, repo, path)
                if path.endswith(".ipynb"):
                    collected_text.append(parse_notebook(content))
                else:
                    collected_text.append(content)
            except:
                continue

    full_text = "\n\n".join(collected_text)

    # TEMP: Save raw extracted content for inspection
    with open("outputs/raw_extracted_content.txt", "w", encoding="utf-8") as f:
        f.write(full_text)

    print("Repository content extracted. Ready for judge evaluation.")

if __name__ == "__main__":
    main()
