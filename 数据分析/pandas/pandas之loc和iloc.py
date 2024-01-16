import numpy as np
import pandas as pd

df = pd.DataFrame(np.arange(12).reshape((3, 4)), index=list("abc"), columns=list("WXYZ"))

print(df)
print(df.loc["a":, "Z"])
print(df.loc[:, "Z"])
print("*" * 100)
print(df.loc[["a", 'b'], "Y":])
print("*" * 100)
# 连续取多行多列
print(df.loc["b":, "Y":])
# iloc基本和np中的取内容相同
df.iloc[1:,:3] = np.nan
print(df)
