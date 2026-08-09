import json
import sys

path = sys.argv[1]

with open(path) as f:
    data = json.load(f)

major, minor, patch = (int(x) for x in data.get("version", "0.0.0").split("."))
data["version"] = f"{major}.{minor}.{patch + 1}"

with open(path, "w") as f:
    json.dump(data, f, indent=2)
    f.write("\n")

print(f"{path} -> {data['version']}")
