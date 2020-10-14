import pandas as pd
for index, row in df.iterrows():
    print(row['A'])

for index, row in df.iterrows():
    print(row[1][0]) # df表第一列