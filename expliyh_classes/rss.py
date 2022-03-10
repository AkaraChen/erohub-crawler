import json
import feedparser
import article
import html5lib
import requests
import time


class RSS:
    def __init__(self, link):
        rss = feedparser.parse(link)
        #print(rss)
        self.articles = []
        for row in rss['entries']:
            title = row['title']
            link = row['link']
            publish_time = row['published_parsed']
            content = row['content'][0]['value']
            tags = []
            categories = []
            try:
                for i in row['tags']:
                    if i['scheme'].find('/categories/') != -1:
                        categories.append(i['term'])
                    elif i['scheme'].find('/tags/') != -1:
                        tags.append(i['term'])
            except KeyError:
                pass

            page = requests.get(link)
            mark1 = page.text.find('<meta property="og:image" content="')
            start = mark1 + len('<meta property="og:image" content="')
            end = page.text.find('">', start)
            cover = page.text[start:end]
            publish_stamp = int(time.mktime(publish_time))
            print(cover)
            self.articles.append(article.Article(title, link, cover, categories, content, publish_stamp))
        print(self.articles[0].date)

    def get_compatible_json(self, per_page, page):
        page0 = []
        st = page * per_page
        for i in range(st, st + per_page):
            dic = self.articles[i].gen_dict()
            js = json.loads(dic)
            page0.append(js)
        return page0
