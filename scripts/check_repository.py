"""Check for accidental local paths, credentials, and notebook errors."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
suffixes = {".py", ".md", ".toml", ".txt", ".yml", ".yaml", ".cff", ".ipynb", ".json", ".csv"}
skip = {".git", ".venv", "__pycache__", ".pytest_cache"}
patterns = {
    "local Windows user path": re.compile(r"[A-Za-z]:[\\/]+Users[\\/]", re.I),
    "private key": re.compile(r"BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY"),
    "secret assignment": re.compile(r"(?i)(?:api[_-]?key|secret|token|password)\s*[:=]\s*['\"][^'\"]{8,}"),
}
allowed = {Path("scripts/check_repository.py")}
failures = []
for path in ROOT.rglob("*"):
    if not path.is_file() or path.suffix.lower() not in suffixes:
        continue
    relative = path.relative_to(ROOT)
    if any(part in skip for part in relative.parts) or relative in allowed:
        continue
    text = path.read_text(encoding="utf-8", errors="ignore")
    for label, pattern in patterns.items():
        if pattern.search(text):
            failures.append(f"{relative}: {label}")
    if path.suffix == ".ipynb":
        data = json.loads(text)
        for cell in data.get("cells", []):
            if not cell.get("id"):
                failures.append(f"{relative}: missing cell id")
            if any(output.get("output_type") == "error" for output in cell.get("outputs", [])):
                failures.append(f"{relative}: saved error output")
if failures:
    raise SystemExit("Repository check failed:\n" + "\n".join(failures))
print("Repository safety check passed.")
