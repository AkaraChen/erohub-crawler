import requests
import json

# Typecho 所在的域名
domain = 'https://api.erohub.org'
# 输出的目录
publicDir = 'dist'
# 下载一轮的数量
pagesize = 50
# 从哪一页开始下
page = 1


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
