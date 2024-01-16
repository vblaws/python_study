import json
# 将python格式数据转化为JSON
data=[{'name':'王硕','age':18},{'name':'王刚','age':112}]
data_json=json.dumps(data,ensure_ascii=False) 
print(type(data_json))
print(data_json)
# JSON转化为python格式数据
s='[{"name": "王硕", "age": 18}, {"name": "王刚", "age": 112}]'
data_python=json.loads(s)
print(type(data_python))
print(data_python)