import yaml
import json


with open("data.yaml", "r") as f:
    print(json.dumps(yaml.load(f), indent=4))
