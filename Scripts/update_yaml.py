import yaml

# Read YAML

with open("../yaml_files/provider.yaml") as f:
    data = yaml.safe_load(f)

# New Access

new_access = {
    "consumer": "DS-TDA-Governance",
    "source": "dev",
    "target": "prod"
}

# Add Access

data["access"].append(new_access)

# Save YAML

with open("../yaml_files/provider.yaml", "w") as f:
    yaml.dump(data, f, sort_keys=False)

print("✅ YAML Updated Successfully")