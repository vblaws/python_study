import os

from pyspark import SparkConf, SparkContext

os.environ["PYSPARK_PYTHON"] = "C:\\Users\\32394\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("set_spark_name")

sc = SparkContext(conf=conf)

# 输入数据
rdd1 = sc.parallelize([1, 2, 3, 4])
# 通过读取文件构建RDD对象
rdd2 = sc.textFile("D:/123.txt")
print(rdd2.collect())
print(rdd1.collect())

# 准备一个RDD
rdd = sc.parallelize([1, 5, 5, 3, 3, 2])


# 通过map方法将每一个元素全部乘以10
# 处理逻辑
def func(data):
	return data * 2


rdd_new = rdd.map(func)

print(rdd_new.collect())
sc.stop()
