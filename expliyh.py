import os
import requests
import feedparser

publicDir = 'expliyh'
pagesize = 12
page = 1

os.system('rm -rf ' + publicDir)
os.mkdir(publicDir)


def requestForData(url):
    r = requests.get(url)
    if r.status_code == 400:
        return False
    else:
        return r.text


def writeFile(name, content):
    f = open(publicDir + '/' + name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


while page <= 100:
    postList = requestForData('https://www.expli.top/wp-json/wp/v2/posts?categories=24&per_page=12&page=' + str(page))
    if not postList:
        break
    writeFile(str(page), str(postList))
    print('第' + str(page) + '页下载好了')
    page += 1
