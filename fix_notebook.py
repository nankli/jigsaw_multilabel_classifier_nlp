import json
import nbformat
from pathlib import Path

def aggressive_fix(input_path, output_path=None):
    input_path = Path(input_path)
    if output_path is None:
        output_path = input_path.with_name(f"fixed_{input_path.name}")

    # Load as raw JSON (even if malformed)
    with open(input_path, "r", encoding="utf-8") as f:
        raw = f.read()

    # Try to strip control characters or invalid JSON fragments
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"[WARN] JSONDecodeError: {e}")
        # Attempt minimal repair: remove bad characters
        raw = raw.replace("\x00", "")
        data = json.loads(raw)

    # Ensure required top-level fields
    if not isinstance(data, dict):
        data = {}
    data.setdefault("cells", [])
    data.setdefault("metadata", {})
    data.setdefault("nbformat", 4)
    data.setdefault("nbformat_minor", 5)

    # Repair each cell if needed
    fixed_cells = []
    for cell in data.get("cells", []):
        if not isinstance(cell, dict):
            continue
        cell.setdefault("cell_type", "code")
        cell.setdefault("metadata", {})
        cell.setdefault("source", [])
        if isinstance(cell["source"], str):
            cell["source"] = [cell["source"]]
        if cell["cell_type"] == "code":
            cell.setdefault("execution_count", None)
            cell.setdefault("outputs", [])
        fixed_cells.append(cell)
    data["cells"] = fixed_cells

    # Repair metadata
    if "kernelspec" not in data["metadata"]:
        data["metadata"]["kernelspec"] = {
            "display_name": "Python 3",
            "language": "python",
            "name": "python3"
        }
    if "language_info" not in data["metadata"]:
        data["metadata"]["language_info"] = {
            "name": "python",
            "version": "3.x"
        }

    # Convert back to nbformat
    nb = nbformat.from_dict(data)

    # Save fixed notebook
    with open(output_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    print(f"[OK] Aggressively fixed notebook saved as {output_path}")


# Example usage
aggressive_fix("Jigsaw_multilabels_BERT.ipynb")

