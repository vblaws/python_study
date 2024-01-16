import string

import pandas as pd

t = pd.Series([1, 2, 1, 32, 123, 123])
print(t)
print(type(t))
t2 = pd.Series([1, 2, 3, 4, 5, 1, 2, 2, 23124, 213], index=list("abcdefhklo"))
print(t2)

# 字典推导试创建一个字典
a = {string.ascii_uppercase[i]: i for i in range(10)}

print(a, type(a))
# 将字典转化为Series
a_Ser = pd.Series(a)
print(a_Ser, type(a_Ser))

# bool操作,将值大于4的显示
print(a_Ser[a_Ser > 4])
# 选中一行
print(a_Ser["E"])
# 取连续多行
print(a_Ser[2:8])
# 取不连续多行
print(a_Ser[["A", "C"]])
