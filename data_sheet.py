import pandas as pd
import openpyxl

data = pd.read_csv("E:\\ML Project\\OWN - Sheet1.csv")
df = pd.DataFrame(data)

col = []

for i in data.columns:
    col.append(i)



for i in range(1,len(col)):
    for j in range(0,len(df[col[i]])):
        if(df[col[i]].values[j] != 0):
            df[col[i]].values[j] = 1


print(df)
df.to_csv("E:\\ML Project\\data.csv")



