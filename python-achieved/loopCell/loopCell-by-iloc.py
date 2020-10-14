# 按行获取每个单元格的内容
for i in range(0, len(df)): #len(df) 行数
    for k in df.iloc(i): #df.iloc[i] 按列获取
        print(k) # 每个单元格的内容


# 已经知道单元格坐标，查询坐标的值
value = df.iloc(0:,0:].values #读几列取第几列的数值（这里是获取全表）
for arr in value:
    for row in arr:
        print(row)