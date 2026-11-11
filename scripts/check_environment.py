from pathlib import Path
import importlib.util
import pandas as pd

root=Path(__file__).resolve().parents[1]
print("Project root:",root)
print("Dataset exists:",(root/"data"/"Dataset.csv").is_file())
print("Dataset size MB:",round((root/"data"/"Dataset.csv").stat().st_size/1024**2,2))
for name in ["numpy","pandas","matplotlib","sklearn"]:
    print(name, bool(importlib.util.find_spec(name)))
