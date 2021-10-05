import os
from math import ceil

import requests
import json

publicDir = 'dist'
pagesize = 12
page = 1

os.system('rm -rf ' + publicDir)
os.mkdir(publicDir)
os.mkdir(publicDir + '/page')
os.mkdir(publicDir + '/post')
os.mkdir(publicDir + '/webpage')


def requestForData(url, response='data'):
    r = requests.get(url)
    if response == 'data':
        return json.loads(r.text)
    else:
        return r.text


def writeFile(name, content, category):
    f = open(publicDir + '/' + category + '/' + name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


# 实际文章数量比获取的少了八个，原因未知
postCount = int(requestForData('https://api.erohub.org/api/count')['data']['counts']) - 8
pageCount = ceil(int(postCount / pagesize) + 2)
print('本次下载共' + str(pageCount) + '页')

while page <= pageCount:
    postList = requestForData('https://api.erohub.org/api/posts?pageSize=' + str(pagesize) + '&page=' + str(page),
                              'origin')
    writeFile(str(page), str(postList), 'page')
    for item in json.loads(postList)['data']:
        cid = item['cid']
        postContent = str(requestForData('https://api.erohub.org/api/post?cid=' + cid, 'origin'))
        writeFile(cid, postContent, 'post')
        print('%s已经下载好了' % item['title'])

    print('第' + str(page) + '页下载好了')
    page += 1

webpage = 1
webpageCount = ceil(int(requestForData('https://api.erohub.org/api/categoryList')['data'][0]['count']) / 12)
print(webpageCount)
while webpage <= webpageCount:
    WebPostList = requestForData('https://api.erohub.org/api/posts?category=2cy&pageSize=12&page=' + str(webpage),
                                 'origin')
    writeFile(str(webpage), str(WebPostList), 'webpage')
    webpage += 1

mzituPage = 1
mzituPageCount = ceil(int(requestForData(requestForData('https://api.erohub.org/api/categoryList')
                                         ['data'][1]['count']) / 12))
print(mzituPageCount)
while mzituPage <= mzituPageCount:
    mzituPostList = requestForData('https://api.erohub.org/api/posts?category=2cy&pageSize=12&page=' + str(webpage),
                                   'origin')
    writeFile(str(mzituPage), str(mzituPostList), 'mzitu')
    mzituPage += 1
