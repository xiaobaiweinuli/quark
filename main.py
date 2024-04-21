import json

from quark import Quark

cookie = ''

quark = Quark(cookie)
quark.set_store_dir("夸克文件夹id")

file_urls = json.load(open("share-data.json", encoding="utf-8"))['data']

for file_item in file_urls:
    print(file_item)
    quark.store(file_item['url'])
