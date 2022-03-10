import json
import time

import feedparser
import requests

import article


class RSS:
    def __init__(self, link):
        rss = feedparser.parse(link)
        # print(rss)
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
            if cover.find("data:image/") != -1:
                cover = ''
            publish_stamp = int(time.mktime(publish_time))
            mark = 0
            for i in categories:
                if i.find("美图"):
                    mark = 1
                    break
            if mark:
                continue
            print("已爬取文章 %s" % title)
            self.articles.append(article.Article(title, link, cover, categories, content, publish_stamp))
        print(self.articles[0].date)

    def get_compatible_json(self, per_page, page):
        page0 = []
        st = page * per_page
        try:
            self.articles[st].gen_dict()
        except IndexError:
            return "啊哈哈哈哈,鸡汤来喽!"
        for i in range(st, st + per_page):
            try:
                dic = self.articles[i].gen_dict()
                page0.append(dic)
            except IndexError:
                break

        js = json.dumps(page0)
        return js
