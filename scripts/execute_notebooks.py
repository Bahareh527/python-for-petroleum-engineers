from pathlib import Path
import os
import nbformat
from nbclient import NotebookClient

ROOT = Path(__file__).resolve().parents[1]
os.environ["PYTHONNOUSERSITE"] = "1"
for path in sorted((ROOT / "notebooks").glob("*.ipynb")):
    notebook = nbformat.read(path, as_version=4)
    NotebookClient(notebook, timeout=300, kernel_name="python3", resources={"metadata": {"path": str(ROOT)}}).execute()
    print(f"OK {path.name}")
