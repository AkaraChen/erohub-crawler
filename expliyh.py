import os
import requests
import rss

publicDir = 'expliyh'
per_page = 12
page = 1

os.system('rm -rf ' + publicDir)
os.mkdir(publicDir)


def request_for_data(url):
    r = requests.get(url)
    if r.status_code == 400:
        return False
    else:
        return r.text


def write_file(name, content):
    f = open(publicDir + '/' + name + '.json', 'w', encoding="utf-8")
    f.write(content)
    f.close()


rss = rss.RSS("https://www.mt6735.top/atom.xml")

for i in range(100):
    js = rss.get_compatible_json(per_page, i)
    if js == "啊哈哈哈哈,鸡汤来喽!":
        break
    write_file(str(i + 1), js)
    print('已写入文件：%s.json' % str(i + 1))

# while page <= 100:
#    postList = requestForData('https://www.expli.top/wp-json/wp/v2/posts?categories=24&per_page=12&page=' + str(page))
#    if not postList:
#        break
#    writeFile(str(page), str(postList))
#    print('第' + str(page) + '页下载好了')
#    page += 1
