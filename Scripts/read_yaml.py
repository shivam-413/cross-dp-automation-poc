import yaml

with open("../yaml_files/provider.yaml") as f:
    data = yaml.safe_load(f)

print(data)
