import numpy as np
import pandas as pd

ones_df = pd.DataFrame(np.ones((2, 4)), index=["A", "B"], columns=list("abcd"))
# print(ones_df)
zeros_df = pd.DataFrame(np.zeros((3, 3)), index=["A", "B", "C"], columns=list("xyz"))
# print(zeros_df)
df1 = ones_df.join(zeros_df)
df2 = zeros_df.join(ones_df)
print(df1)
print("*" * 100)
print(df2)
