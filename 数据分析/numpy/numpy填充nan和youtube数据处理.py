import numpy as np

t1 = np.arange(12).reshape((3, 4,)).astype(float)
t1[1, 2:] = np.nan
print(t1)


# 填充nan值
def fill_is_null(t1):
	for i in range(t1.shape[1]):  # 求出有多少列
		temp_col = t1[:, i]  # 当前列
		nan_num = np.count_nonzero(temp_col != temp_col)  # 求出当前列有nan的个数
		if nan_num != 0:  # 如果nan_num!=0说明此列内有nan出现
			temp_not_nan_col = temp_col[temp_col == temp_col]  # 当前一列不为nan的array
			temp_col[np.isnan(temp_col)] = np.mean(temp_not_nan_col)  # 将此列中为nan的值修改为此列的平均值
	return t1


if __name__ == '__main__':
	print(fill_is_null(t1))
