import json

json_data = '{"name": "Brain", "city": "Phnom Penh"}'
python_obj = json.loads(json_data)
print(python_obj["name"])
print(python_obj["city"])
