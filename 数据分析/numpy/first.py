import numpy as np

a = np.arange(1, 6, 2)
print(a)

t2 = np.array([[1, 2, 3], [4, 5, 6]])
print(t2.shape)

t4 = np.arange(12)
print(t4.reshape(3, 2, 2))

t5 = np.arange(20).reshape((2, 5, 2))
print(t5)
print(t5.reshape((20,1)))
# 将数据变成一维的
print(t5.flatten())
