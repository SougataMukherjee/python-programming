import json

data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "courses": ["Python", "Data Science"]
}


print(json.dumps(data))
pretty_json = json.dumps(data, indent=4, sort_keys=True)
print(pretty_json)