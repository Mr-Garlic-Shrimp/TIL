import pandas as pd

list1 = [12, 24, 35]
index1 = ['Row1', 'Row2', 'Row3']
# create 1D array
s = pd.Series(data=list1, index=index1)
#print(s)

# create 1D array from dict.
dict1 = dict(Row1=11, Row2=22, Row=33)
d = pd.Series(data=dict1)
#print(d)


# extract from DataFrame
list2 = [[1, 2, 3], [21, 22, 23], [31, 32, 33]]
columns1 = ['Col1', 'Col2', 'Col3']
df1 = pd.DataFrame(data=list2, index=index1, columns=columns1)
print(df1)

print(df1['Col2'])

ser1 = df1['Col2']
print(ser1['Row2'])
print(ser1 >= 20)
# SeriesではTrueのデータのみ表示する
print(ser1[ser1 >= 20])

# df2 = pd.DataFrame(ser1)
# print(df2)

