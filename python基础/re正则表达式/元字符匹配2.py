# 只能由字母和数字组成，长度为6-10
import re

r = '^[0-9a-zA-Z]{6,10}$'
s = "1234567"
print(re.findall(r, s))
# 匹配qq号,要求为数字,长度为5-11，第一位不为零
r1 = '^[1-9][0-9]{4,10}$'
print(re.findall(r1, s))
