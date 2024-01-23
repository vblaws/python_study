import pandas as pd
from matplotlib import pyplot as plt

pd.set_option("display.max_columns", None)
# pd.set_option("display.max_rows", None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\books.csv"
df = pd.read_csv(file_path)
print(df.head())
print(df.info())
# 按行删除,会删除需要的数据
# df = df.dropna(axis=0)
data_series = df[pd.notnull(df["original_publication_year"])]
print(type(data_series))
print(data_series.head())

different_year_book = data_series.groupby(by="original_publication_year")["title"].count()
print(different_year_book)
_x = different_year_book.index
_y = different_year_book.values
plt.figure(figsize=(20, 8), dpi=80)
# plt.bar(_x,_y)
plt.plot(_x,_y)
plt.show()