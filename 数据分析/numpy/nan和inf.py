import numpy as np

t = np.arange(1, 4).astype(float)
print(t)
t[2] = np.nan
print(t)

print("#" * 100)
t3 = np.arange(24).reshape((4, 6,)).astype(float)

t3[:, 0] = 0
t3[3, 3] = np.nan
print(t3)
print("为nan的个数:", np.count_nonzero(t3 != t3))

print(t.sum())
print(t3.sum(axis=0))
