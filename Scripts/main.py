
import json
import pandas as pd
import yaml

print("PR Test Change\n")
print("========== CROSS DP AUTOMATION ==========\n")

# STEP 1 - Read Request

with open("../input/request.json") as f:
    request = json.load(f)

consumer = request["consumer"]
provider = request["provider"]
access = request["access"]

print("Request Received")

print("Consumer :", consumer)
print("Provider :", provider)
print("Access   :", access)

# STEP 2 - Clean Name

provider = provider.replace("_", "-")
provider = provider.replace("-LH", "")

print("\nValidated Provider :", provider)

# STEP 3 - Owner Lookup

df = pd.read_csv("../lookup/owner.csv")

result = df[df["data_product"] == provider]

if len(result) > 0:

    owner = result.iloc[0]["owner"]

    print("\nOwner Found :", owner)

else:

    print("\nOwner Not Found")

# STEP 4 - Read YAML

with open("../yaml_files/provider.yaml") as f:
    yaml_data = yaml.safe_load(f)

# STEP 5 - Access Check

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

if found:

    print("\n✅ Access Already Exists")

else:

    print("\n❌ Access Not Found")

    yaml_data["access"].append(
        {
            "consumer": consumer,
            "source": source,
            "target": target
        }
    )

    with open("../yaml_files/provider.yaml", "w") as f:

        yaml.dump(yaml_data, f, sort_keys=False)

    print("✅ YAML Updated\n")
    print("Second PR Test")