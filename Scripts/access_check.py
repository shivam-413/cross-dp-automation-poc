import yaml

with open("../yaml_files/provider.yaml") as f:
    data = yaml.safe_load(f)

consumer = "DS-TDA-Governance"
source = "dev"
target = "prod"

found = False

for item in data["access"]:

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