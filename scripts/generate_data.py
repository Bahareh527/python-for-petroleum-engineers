from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from petroleum_python.synthetic import write_course_data
write_course_data(ROOT / "data", seed=42)
print("Synthetic course data regenerated.")
