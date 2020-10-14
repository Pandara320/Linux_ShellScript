import pandas as pd

d = {'目前成材率': pd.Series([0.9756, 0.8961, 0.9688], index=['2020年8月9日-1', '2020年8月10日', '012220']),
     '要求成材率': pd.Series([0.955, 0.955, 0.955], index=['2020年8月9日-1', '2020年8月10日', '012220'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

# print ("Adding a new column by passing as Series:")
# df['test3']=pd.Series([10,20,30],index=['a','b','c'])
# print(df)

print("用之前两列的数据计算-增加一列 计算成材率:")
df['结余'] = df['目前成材率'] - df['要求成材率']

print(df)

# case test design for df
# data = [{'日期': 1, 'x': 2},{'a': 5, 'b': 10, 'c': 20}]
#
