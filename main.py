import requests
import json

domain = 'https://api.erohub.org'
publicDir = 'dist'
pagesize = 12


def requestForData(url):
    r = requests.get(url)
    result = json.loads(r.text)
    data = result
    return data


def writeFile(name, content, category):
    f = open(publicDir + '/' + category + '/' + name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


# 实际文章数量比获取的少了八个，原因未知
postCount = int(requestForData(domain + '/api/count')['data']['counts']) - 8
pageCount = int(postCount / pagesize) + 1
print('本次下载共' + str(pageCount) + '页')

page = 25
while page <= pageCount:
    postList = requestForData(domain + '/api/posts?pageSize=' + str(pagesize) + '&page=' + str(page))
    for item in postList['data']:
        cid = item['cid']
        postContent = str(requestForData(domain + '/api/post?cid=' + cid))
        writeFile(cid, postContent, 'post')
        print(item['title'] + '已经下载好了')

    print('第' + str(page) + '页下载好了')
    page += 1
