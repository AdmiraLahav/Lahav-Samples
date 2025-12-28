import json

# Read from file and parse JSON
with open("./example.json", "r") as f:
    data = json.load(f)

print(data)
print(type(data))