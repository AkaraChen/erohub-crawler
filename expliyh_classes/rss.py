import json
import feedparser
import article
import html5lib
import requests


class RSS:
    def __init__(self, link):
        rss = feedparser.parse(link)
        #        print(rss)
        self.articles = []
        for row in rss['entries']:
            title = row['title']
            link = row['link']
            publish_time = row['published']
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
            print(cover)
            self.articles.append(article.Article(title, link, cover, categories, content))
        print(self.articles[0].gen_dict())
