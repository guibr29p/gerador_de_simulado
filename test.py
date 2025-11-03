import json
import pandas as pd



path = "data/collection/test1/test.json"

df = pd.read_json(path_or_buf=path, orient="records")

print(df.get("question"))