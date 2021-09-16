import os
import requests
import json

domain = 'https://api.erohub.org'
publicDir = 'dist'
pagesize = 12
page = 1

os.system('rm -rf '+publicDir)
os.mkdir(publicDir)
os.mkdir(publicDir + '/page')
os.mkdir(publicDir + '/post')


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
postCount = int(requestForData(domain + '/api/count')['data']['counts']) - 8
pageCount = int(postCount / pagesize) + 2
print('本次下载共' + str(pageCount) + '页')

while page <= pageCount:
    postList = requestForData(domain + '/api/posts?pageSize=' + str(pagesize) + '&page=' + str(page), 'origin')
    writeFile(str(page), str(postList), 'page')
    for item in json.loads(postList)['data']:
        cid = item['cid']
        postContent = str(requestForData(domain + '/api/post?cid=' + cid, 'origin'))
        writeFile(cid, postContent, 'post')
        print('%s已经下载好了' % item['title'])

    print('第' + str(page) + '页下载好了')
    page += 1
