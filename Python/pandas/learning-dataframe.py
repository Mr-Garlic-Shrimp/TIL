import pandas as pd

df_sales = pd.read_csv('Sales-sample.csv', index_col=['Sales_No'])
# dirを指定
#df_sales = pd.read_csv(r'C:\Users\1stel\Downloads\T_Sales_Header (1).csv', index_col=['Sales_No'])
print(df_sales.iloc[3:6, 0:2])

