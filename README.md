# quark
夸克网盘转存分享一体化

由于用到了sqlite，对多线程的兼容性一般，建议不要使用多线程运行

# 示例
```python
import json

from quark import Quark

cookie = 'xxxx'

quark = Quark(cookie)
quark.set_store_dir("视频转存")

file_urls = json.load(open("share-data.json", encoding="utf-8"))['data']

for file_item in file_urls:
    print(file_item)
    quark.store(file_item['url'])
```