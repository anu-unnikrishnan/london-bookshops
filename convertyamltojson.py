import json
import yaml
stream = open("bookshops.yaml", "r")
output = open("bookshops.json", "a")
data = yaml.safe_load_all(stream)
for yaml_doc in data:
    json.dump(yaml_doc, output, indent = 1)
