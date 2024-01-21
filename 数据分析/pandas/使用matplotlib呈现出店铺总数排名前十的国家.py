import pandas as pd

# 设置显示所有的列,
pd.set_option("display.max_columns", None)

file_path = "D:\\EageDownload\\DataAnalysis-master\\day05\\code\\starbucks_store_worldwide.csv"

df = pd.read_csv(file_path)

