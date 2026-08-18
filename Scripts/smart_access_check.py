import json
import yaml

# Read Request

with open("../input/request.json") as f:
    request = json.load(f)

# Read YAML

with open("../yaml_files/provider.yaml") as f:
    yaml_data = yaml.safe_load(f)

consumer = request["consumer"]

access = request["access"]

source = access.split("_to_")[0]
target = access.split("_to_")[1]

found = False

for item in yaml_data["access"]:

    if (
        item["consumer"] == consumer
        and item["source"] == source
        and item["target"] == target
    ):
        found = True
        break

if found:
    print("✅ Access Already Exists")

else:
    print("❌ Access Not Found")