import numpy as np
import pandas as pd

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"
# 让打印出来的结果没有省略号
pd.set_option('display.max_columns', None)

df = pd.read_csv(file_path)
# Genre表示类型的意思
temp_list = df["Genre"].str.split(",").tolist()  # [[],[],[]]

# print(df["Genre"].head(3))
# 取出电影的所有种类放在同一个列表里面
genre_data = list(set([i for j in temp_list for i in j]))  # 先转换为集合去重,然后转换为列表

# 构造全为0的数组,列数为每一个种类
zero_list = pd.DataFrame(np.zeros((df.shape[0], len(genre_data))), columns=genre_data)
# print(df)
# range内可以写len(temp_list)或者df.shape(0),因为len(temp_list)长度等于df.shape[0]的行数
for i in range(df.shape[0]):
	# zero_list.loc[0,["Sci-fi","Music"]]=1
	zero_list.loc[i, temp_list[i]] = 1

print(zero_list)

# 统计每一个分类的电影的数量和
print(zero_list.sum(axis=0))
# axis=0：表示沿着行的方向进行操作。在二维数组中，这相当于垂直向下。对于一维数组来说，这个参数没有意义，因为它只有一个轴。对于二维数组来说，axis=0通常表示按照列的方向进行操作。
# axis=1：表示沿着列的方向进行操作。在二维数组中，这相当于水平延申。对于一维数组来说，这个参数也没有意义。对于二维数组来说，axis=1通常表示按照行的方向进行操作。

# 当然可以，这段代码主要是用来处理一个电影数据集，并对每个电影的类型进行编码。以下是代码的详细解释：
#
# 导入必要的库:
#
# python
# import numpy as np
# import pandas as pd
# 导入NumPy和Pandas库。NumPy用于数值计算，而Pandas用于数据处理。
# 2. 设置文件路径:
#
# python
# file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\IMDB-Movie-Data.csv"
# 这行代码定义了一个文件路径，指向一个CSV文件。这个文件应该包含电影数据。
# 3. 设置Pandas显示选项:
#
# python
# pd.set_option('display.max_columns', None)
# 设置Pandas的显示选项，使其在打印DataFrame时显示所有列。
# 4. 读取CSV文件:
#
# python
# df = pd.read_csv(file_path)
# 使用Pandas的read_csv函数读取CSV文件，并将数据存储在DataFrame对象df中。
# 5. 处理"Genre"列:
#
# python
# temp_list = df["Genre"].str.split(",").tolist()  # [[],[],[]]
# genre_data = list(set([i for j in temp_list for i in j]))  # 先转换为集合去重,然后转换为列表
# * `temp_list = df["Genre"].str.split(",").tolist()`：将"Genre"列中的数据按逗号分隔，并将结果转换为列表。例如，如果某行的"Genre"列是"Action,Comedy"，那么这一行在`temp_list`中的值就是["Action", "Comedy"]。
# * `genre_data = list(set([i for j in temp_list for i in j]))`：这是一个列表推导式，用于从`temp_list`中提取唯一的元素（即去重）。这意味着如果有多个电影被标记为"Action"，那么"Action"只会在`genre_data`中出现一次。
# 6. 创建一个全为0的DataFrame:
#
# python
# zero_list = pd.DataFrame(np.zeros((df.shape[0], len(genre_data))), columns=genre_data)
# 创建一个新的DataFrame，其形状与原始数据集的行数相同，列数为genre_data的长度。所有值都初始化为0。列名由genre_data提供。
# 7. 更新DataFrame的值:
# 对于原始数据集中的每一行，根据其"Genre"值在新的DataFrame中相应的位置上设置为1。这是通过以下循环完成的：
#
# python
# for i in range(df.shape[0]):
#     zero_list.loc[i, temp_list[i]] = 1
# 打印结果:
# 最后，打印处理后的数据集和原始数据集。结果是一个新的DataFrame，其中每一行表示原始数据集中的一行，列表示不同的电影类型，值为1表示该行对应的电影具有该类型，否则为0。原始数据集也打印出来，以便于比较和验证。
