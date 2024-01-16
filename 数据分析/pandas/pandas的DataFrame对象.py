import numpy as np
import pandas as pd

t = pd.DataFrame(np.arange(24).reshape((4, 6,)), index=list("abcd"), columns=list("ABCDEF"))
print(t)
print(t.sum(axis=1))
d1 = {"name": ["xiaoming", "xiaogang"], "age": [20, 32], "tel": [10086, 10010]}
df = pd.DataFrame(d1)
print(df)
print("行索引", df.index)
print("列索引", df.columns)
print("*" * 100)
print(df.shape)
print("*" * 100)
print(df.dtypes)
print("*" * 100)
print(df.info())
print("*" * 100)
print(df.describe())