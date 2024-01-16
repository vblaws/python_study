import numpy as np

t = np.arange(24).reshape((4, 6,))

print(t)
# 行交换
t[[0, 1], :] = t[[1, 0], :]
print(t)

t1 = np.arange(25,49).reshape((4, 6,))

print(np.vstack((t, t1)))
