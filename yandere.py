import os
import requests

publicDir = 'yandere'
pagesize = 12
page = 1

os.system('rm -rf ' + publicDir)
os.mkdir(publicDir)


def requestForData(url):
    r = requests.get(url)
    return r.text


def writeFile(name, content):
    f = open(publicDir + '/' + name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


while page <= 100:
    postList = requestForData('https://yande.re/post.json?limit=12&tags=rating%3As&page=' + str(page))
    writeFile(str(page), str(postList))
    print('第' + str(page) + '页下载好了')
    page += 1