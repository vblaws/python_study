import pandas as pd

df = pd.read_csv("D:\\EageDownload\\dogNames2.csv")

print(df.head())
print(df.info())

df = df.sort_values(by="Count_AnimalName", ascending=False)
print(df.head())
print(df[:20]["Row_Labels"])
print("*" * 100)
print(df[df["Count_AnimalName"] > 800])
print("*" * 100)
print(df[(df["Count_AnimalName"] > 800) & (df["Count_AnimalName"] < 1000)])
print("名字长度大于4并且使用次数超过700次的宠物:")
print(df[(df["Row_Labels"].str.len() > 4) & (df["Count_AnimalName"] > 700)])
print("*" * 100)
print(df["Count_AnimalName"])
print(pd.notnull(df))
#