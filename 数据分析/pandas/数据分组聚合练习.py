import pandas as pd

# 设置显示所有的列,
pd.set_option("display.max_columns", None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
print(df.head())
print(df.info())
print("*" * 100)
# print(df.groupby(by="Country"))
# print(type(df.groupby(by="Country")))
# DataFrameGroupBy可以进行遍历
# 可以调用聚合方法
groupby_Country = df.groupby(by="Country")

for i in groupby_Country:
	# print("*" * 100)
	# if i[0] == "US":
	# 	print(i[1])
	print(i[1])
	print('-----------')
	print(i[0])
	print("++++++++++++")

country_size = groupby_Country["Brand"].count()
# print(type(country_size))
# 取行
print(country_size["US"])
print(country_size["CN"])
for i in range(10):
	print("*" * 100)
# 统计中国每个省份店铺的数量
china_data = df[df["Country"] == "CN"]

print(china_data)
print(china_data.info())
# 按照省份分组，并且计算有多少个店铺
china_groupd = china_data.groupby(by="State/Province")["Brand"].count()
[print("*" * 100) for i in range(100)]
# 数据按照多个条件进行分组
groupd=df["Brand"].groupby(by=[df["Country"],df["State/Province"]]).count()
print(groupd)
print(type(groupd))




groupd=df[["Brand"]].groupby(by=[df["Country"],df["State/Province"]]).count() # 错误Brand是一个Series没有Country和state/Province
