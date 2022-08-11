# Ref: https://linuxhint.com/plot-data-pandas-python/

import matplotlib.pyplot as plt
import pandas as pd
# 日本語をグラフに表示できるようにする。
plt.rcParams['font.family'] = "MS Gothic"

gdp_cal = {
    'GDP_growth': [6.1, 5.8, 5.7, 5.7, 5.8, 5.6, 5.5, 5.3, 5.2, 5.2],
    'Oil_Price': [1500, 1520, 1525, 1523, 1515, 1540, 1545, 1560, 1555, 1565]
}
print(gdp_cal)

df = pd.DataFrame(data=gdp_cal, columns=['Oil_Price', 'GDP_growth'])
print(df)

df.plot(x='Oil_Price', y='GDP_growth', kind='scatter', color='red')
plt.title('Title')
plt.xlabel('X軸')
plt.ylabel('Y軸')
plt.show()
