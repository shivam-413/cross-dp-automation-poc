import json
import pandas as pd

# Read Request

with open("../input/request.json") as f:
    request = json.load(f)

provider = request["provider"]

# Cleaning Logic

provider = provider.replace("_", "-")
provider = provider.replace("-LH", "")

print("Provider Name:", provider)

# Read Owner Table

df = pd.read_csv("../lookup/owner.csv")

# Find Owner

result = df[df["data_product"] == provider]

if len(result) > 0:

    print("\n✅ Owner Found")

    print("Owner:", result.iloc[0]["owner"])

    print("Email:", result.iloc[0]["email"])

else:

    print("\n❌ Owner Not Found")