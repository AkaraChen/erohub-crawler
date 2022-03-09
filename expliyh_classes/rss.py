import json
import feedparser
import article
import html5lib
import requests


class RSS:
    def __init__(self, link):
        rss = feedparser.parse(link)
        print(rss)
        articles = []
        for row in rss['entries']:
            title = row['title']
            link = row['link']
            publish_time = row['published']
            content = row['content']['value']
            tags = []
            categories = []
            for i in row['tags']:
                if i['scheme'].find('/categories/') is not -1:
                    categories.append(i['term'])
                elif i['scheme'].find('/tags/') is not -1:
                    tags.append(i['term'])
            page = requests.get(link)
            mark1 = page.text.find('<meta property="og:image" content="')
            start = mark1 + len('<meta property="og:image" content="')
            end = page.text.find('">', start)
            cover = page.text[start:end]
