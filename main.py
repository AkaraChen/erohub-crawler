import requests
import json

# Typecho 所在的域名
domain = 'https://api.erohub.org'
# 输出的目录
publicDir = 'dist'
# 下载一轮的数量
pagesize = 12
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


# 实际文章数量比获取的少了八个，原因未知
postCount = int(requestForData(domain + '/api/count')['data']['counts']) - 8
pageCount = int(postCount / pagesize) + 1
print('本次下载共' + str(pageCount) + '页')

while page <= pageCount:
    postList = requestForData(domain + '/api/posts?pageSize=' + str(pagesize) + '&page=' + str(page), 'origin')
    writeFile(str(page), str(postList), 'page')
    print('第%s页下载好了' % page)
    # for item in postList['data']:
    #     cid = item['cid']
    #     postContent = str(requestForData(domain + '/api/post?cid=' + cid, 'origin'))
    #     writeFile(cid, postContent, 'post')
    #     print('%s已经下载好了' % item['title'])
    #
    # print('第' + str(page) + '页下载好了')
    page += 1
