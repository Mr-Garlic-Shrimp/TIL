# 2022年8月4日　朝活
# 参考サイト：https://ai-inter1.com/python-webscraping/
import requests
from bs4 import BeautifulSoup
# 正規表現で文字列検索できるようにするモジュールre
import re


url = 'https://news.yahoo.co.jp'
response = requests.get(url)
# htmlファイルの中身を表示
#print(response.text[:500])
#print(response.text)

soup = BeautifulSoup(response.text, 'html.parser')
# htmlの中身をhrefの特定文字列で検索し、ヒットした結果のリストを返す
elems = soup.find_all(href=re.compile('news.yahoo.co.jp/pickup'))
print(elems[0])
# hrefでヒットしたaタグのコンテンツを取得
# print(elems[0].contents[0])
# print(elems[1].contents[0])
#
# print(elems[0].attrs['href'])

for elem in elems:
    print(elem.contents[0])
    print(elem.attrs['href'])
