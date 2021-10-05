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


