import re

s = "python itheima python itheima python itheima python itheima python itheima"

result = re.match("python", s)
print(result)
print(result.span())
print(result.group())
s1 = "sjkfppythonasdfhhjhkjhkpython"
result1 = re.search("python", s1)
print(result1)
print(result1.span())
print(result1.group())

result2 = re.findall("python", s1)
print(result2)
email = "H3239498031@gmail.com"
rule = r'^[\w-]+(\.[\w-]+)*@(qq|162|gmail)(\.[\w-]+)+$'
print(re.match(rule, email))
