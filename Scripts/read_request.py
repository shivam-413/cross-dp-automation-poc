import json

with open("../input/request.json") as f:
    request = json.load(f)

print("Consumer:", request["consumer"])
print("Provider:", request["provider"])
print("Access:", request["access"])