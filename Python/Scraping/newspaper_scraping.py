# Ref:https://ai-inter1.com/webscraping_newspaper_2/

import newspaper
import nltk
nltk.download('punkt')
import csv
import datetime


url = 'https://www.bloomberg.co.jp/'

website = newspaper.build(url, memoize_articles=False, MAX_SUMMARY=300)

for article in website.articles:
    print(article.url)
    print(article.title)

# create summary, then export to csv
csv_date = datetime.datetime.today().strftime('%Y%m%d')
csv_file_name = 'bloomberg_' + csv_date + '.csv'

with open(csv_file_name, 'w', newline='', encoding='cp932') as csvfile:
    w = csv.writer(csvfile, delimiter=',', lineterminator='\n')
    csv_header = ['Article No.', 'URL', "Summary"]
    w.writerow(csv_header)

    for item in range(len(website.articles)):
        # 一行書くごとにリストは初期化される
        csvlist = []
        website_article = website.articles[item]
        website_article_url = website_article.url
        try:
            website_article.download()
            website_article.parse()
            website_article.nlp()
            # 記事のサマリを取得
            print("記事[" + str(item) + "]: " + website_article_url + " : "
                  + website_article.summary + "\n")
            csvlist.append(str(item))
            csvlist.append(website_article.url)
            csvlist.append(website_article.summary)
            w.writerow(csvlist)
        except:
            print("記事[" + str(item) + "]: " + website_article_url + " : "
                  + "取得エラー" + "\n")
            continue




# from newspaper import Article
#
#
# url = 'https://www.japantimes.co.jp/news/2019/07/19/national/top-japanese-comedian-retire-wake-underground-business-scandal/#.XTKwtnduKP8'
#
# article = Article(url)
# article.download()
# article.parse()
#
# print(article.publish_date)
# print(article.authors)
# print(article.text)
#
# import nltk
# nltk.download('punkt')
# article.nlp()
# print(article.keywords)
# print(article.summary)