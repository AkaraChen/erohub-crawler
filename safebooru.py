import xmltodict
import requests
import json
import os

publicDir = 'safebooru'
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
    postList = json.dumps(xmltodict.parse(
        requestForData('https://safebooru.org/index.php?page=dapi&s=post&q=index&limit=12&pid=' + str(page)))).replace(
        "@", "")
    writeFile(str(page), str(postList))
    print('第' + str(page) + '页下载好了')
    page += 1
