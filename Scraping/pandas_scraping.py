# 2022年8月4日　朝活
# 参考サイト：https://ai-inter1.com/python-webscraping/
#           https://otoha0510.hatenablog.com/entry/2017/11/04/021207

import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
# matplotlibで日本語表示できるようにする
plt.rcParams['font.family'] = "MS Gothic"

# 指定URLから表をDataFrameとして入手
url = 'https://stocks.finance.yahoo.co.jp/stocks/history/?code=2282.T'
print(url)
data = pd.read_html(url, header=0)


# テーブルが二つある場合、左のインデックスは1以上になる
# print(data[0].head())
# print(data[0].tail())
#
print(data[0]["日付"])
# print(data[0]["始値"])

# data[0]["日付"]に格納されている値（文字列）をiに読み込み、strptimeで日付型に変換して新しい列’日付２’を定義
data[0]["日付2"] = [dt.strptime(i, "%Y年%m月%d日") for i in data[0]["日付"]]
print(data[0]['日付2'].head())

# 列’日付2’をインデックス（主キー的なもの）として追加
data[0].set_index('日付2', inplace=True)
print(data[0].head())

#data[0]["終値"].plot(title='株価',grid=True)

# indexの列は暗黙的にx軸になる模様
data[0].plot(y='終値', title='株価')

# x軸を明示的に指定
#data[0].plot(x='始値', y='終値', title='株価')

# 軸、タイトル名は明示的に指定した方が確実かも）
plt.title('株価')
plt.xlabel('日付2')
plt.ylabel('終値')

# pycharmでグラフを描画する場合、matplotlib.pyplotをインポートしてshowメソッドを呼び出す必要あり。
plt.show()

data[0].to_csv('stock.csv')