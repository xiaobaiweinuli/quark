import json

from quark import Quark

cookie = 'xxx'

quark = Quark(cookie)
quark.set_store_dir("视频转存")

file_urls = json.load(open("share-data.json", encoding="utf-8"))['data']

for file_item in file_urls:
    print(file_item)
    quark.store(file_item['url'])
