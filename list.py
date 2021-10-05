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
os.mkdir(publicDir + '/mzitu')


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


webpage = 1
webpageCount = ceil(int(requestForData('http://api.erohub.org/api/categoryList')['data'][0]['count']) / 12)
print(webpageCount)
while webpage <= webpageCount:
    WebPostList = requestForData('http://api.erohub.org/api/posts?category=2cy&pageSize=12&page=' + str(webpage),
                                 'origin')
    writeFile(str(webpage), str(WebPostList), 'webpage')
    webpage += 1

mzituPage = 1
mzituPageCount = ceil(int(requestForData('http://api.erohub.org/api/categoryList')['data'][1]['count']) / 12)
print(mzituPageCount)
while mzituPage <= mzituPageCount:
    mzituPostList = requestForData('http://api.erohub.org/api/posts?category=2cy&pageSize=12&page=' + str(mzituPage),
                                   'origin')
    writeFile(str(mzituPage), str(mzituPostList), 'mzitu')
    mzituPage += 1
