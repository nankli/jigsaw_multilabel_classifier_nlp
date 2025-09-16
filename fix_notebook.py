import nbformat
import json
import sys
from pathlib import Path

def fix_notebook(input_path, output_path=None):
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_name(f"fixed_{input_path.name}")
    
    try:
        # Try to read as a proper notebook
        with open(input_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
    except Exception as e:
        print(f"[ERROR] Could not parse with nbformat directly: {e}")
        # Try raw JSON repair
        with open(input_path, "r", encoding="utf-8") as f:
            raw = json.load(f)

        # Ensure required fields
        raw.setdefault("cells", [])
        raw.setdefault("metadata", {})
        raw.setdefault("nbformat", 4)
        raw.setdefault("nbformat_minor", 5)

        # Add default kernelspec if missing
        if "kernelspec" not in raw["metadata"]:
            raw["metadata"]["kernelspec"] = {
                "display_name": "Python 3",
                "language": "python",
                "name": "python3"
            }
        # Add language info if missing
        if "language_info" not in raw["metadata"]:
            raw["metadata"]["language_info"] = {
                "name": "python",
                "version": "3.x"
            }

        nb = nbformat.from_dict(raw)

    # Save repaired notebook
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"[OK] Fixed notebook saved as {output_path}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python fix_notebook.py your_notebook.ipynb")
    else:
        fix_notebook(sys.argv[1])

