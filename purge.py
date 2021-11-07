import os
import sys
from math import ceil
import requests
import json

domain = 'http://' + sys.argv[1]
publicDir = 'dist'
pagesize = 12
page = 1


def requestForData(url, response='data'):
    r = requests.get(url)
    if response == 'data':
        return json.loads(r.text)
    else:
        return r.text


def writeFile(name, content, category):
    f = open(publicDir + '/' + category + '/' +
             name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


# 实际文章数量比获取的少了八个，原因未知
postCount = int(requestForData(domain + '/api/count')['data']['counts']) - 8
pageCount = ceil(int(postCount / pagesize) + 2)
print('本次下载共' + str(pageCount) + '页')

while page <= pageCount:
    postList = requestForData(domain + '/api/posts?pageSize=' + str(pagesize) + '&page=' + str(page),
                              'origin')
    requests.get("https://cdn.jsdelivr.net/gh/AsahiIndustry/erohub-backend@latest/dist/page/"+str(page)+".json")
    page += 1

webpage = 1
webpageCount = ceil(
    int(requestForData(domain + '/api/categoryList')['data'][0]['count']) / 12)
print(webpageCount)
while webpage <= webpageCount:
    WebPostList = requestForData(domain + '/api/posts?category=2cy&pageSize=12&page=' + str(webpage),
                                 'origin')
    requests.get("https://cdn.jsdelivr.net/gh/AsahiIndustry/erohub-backend@latest/dist/webpage/"+str(webpage)+".json")
    webpage += 1

requests.get("https://cdn.jsdelivr.net/gh/AsahiIndustry/erohub-backend@latest/dist/webpage/manifest.json")


mzituPage = 1
mzituPageCount = ceil(
    int(requestForData(domain + '/api/categoryList')['data'][1]['count']) / 12)
print(mzituPageCount)
while mzituPage <= mzituPageCount:
    mzituPostList = requestForData(domain + '/api/posts?category=mzitu&pageSize=12&page=' + str(mzituPage),
                                   'origin')
    requests.get("https://cdn.jsdelivr.net/gh/AsahiIndustry/erohub-backend@latest/dist/mzitu/"+str(mzituPage)+".json")
    mzituPage += 1

requests.get("https://cdn.jsdelivr.net/gh/AsahiIndustry/erohub-backend@latest/dist/mzitu/manifest.json")

