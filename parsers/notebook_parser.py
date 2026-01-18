import json

def parse_notebook(text):
    nb = json.loads(text)
    content = []
    for cell in nb.get("cells", []):
        if cell["cell_type"] in ["markdown", "code"]:
            content.append("".join(cell.get("source", [])))
    return "\n".join(content)
