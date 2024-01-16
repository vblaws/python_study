import re

Str = "iasdfhu2309230-af[;asdADAWSADoa]sdf\adf=-r-3230-iasdfusocvhashfeoau329hasdfoi"
result = re.findall(r'\d', Str)  # 匹配所有数字
print(result)
special = re.findall(r'\W', Str)  # 匹配所有特殊字符
print(special)
english = re.findall(r'[a-zA-Z]', Str)  # 匹配所有英文字符
print(english)


