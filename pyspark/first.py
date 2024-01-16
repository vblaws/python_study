# 导包
from pyspark import SparkConf, SparkContext

# 创建SparkConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")  # 给spark程序起了一个名字
# 基于SparkConf类对象创建SparkContext类对象
sc = SparkContext(conf=conf)
# 打印版本
print(sc.version)

# 关闭运行
sc.stop()
