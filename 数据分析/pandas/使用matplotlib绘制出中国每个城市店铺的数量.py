import pandas as pd
from matplotlib import pyplot as plt
from pylab import mpl

mpl.rcParams["font.sans-serif"] = ["SimHei"]

pd.set_option('display.max_columns', None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)
china_data = df[df["Country"] == "CN"]
#
# print(china_data)
province_data = china_data.groupby(by="City")["Brand"].count()[:10]

print(type(province_data))
_x = province_data.index
_y = province_data.values

plt.figure(figsize=(20, 8), dpi=80)
plt.barh(_x, _y,height=0.3)
# plt.xticks(_x,rotation=90)

plt.show()
