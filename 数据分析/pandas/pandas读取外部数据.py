import pandas as pd
from pymongo import MongoClient
df = pd.read_csv("D:\\EageDownload\\DataAnalysis-master\\day05\\code\\books.csv")

print(df)
print(type(df))