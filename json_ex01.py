import json


data_json = '{"name": Carlos','age': 42, 'course': "Data Analytics"}''

data_dict = json.loads(data_json)

print(data_dict)