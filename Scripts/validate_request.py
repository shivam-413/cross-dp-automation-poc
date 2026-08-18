import json

# Read Request

with open("../input/request.json") as f:
    request = json.load(f)

provider = request["provider"]

print("Original Name:")
print(provider)

# Replace underscore with hyphen

provider = provider.replace("_", "-")

# Remove LH

provider = provider.replace("-LH", "")

print("\nCleaned Name:")
print(provider)

# Validation

if provider.startswith(("DS-", "CADP-")):
    print("\n✅ Valid Data Product")
else:
    print("\n❌ Invalid Data Product")
