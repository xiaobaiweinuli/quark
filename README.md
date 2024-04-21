# 新增
自动把合集里的数据转成json格式进行转存，分享，导出，推到Github
相应项目：[https://github.com/xiaobaiweinuli/duanju](https://github.com/xiaobaiweinuli/duanju)
# quark
夸克网盘转存分享一体化

由于用到了sqlite，对多线程的兼容性一般，建议不要使用多线程运行

# 示例
```python
import json

from quark import Quark

cookie = 'xxxx'

quark = Quark(cookie)
quark.set_store_dir("夸克文件夹id")

file_urls = json.load(open("share-data.json", encoding="utf-8"))['data']

for file_item in file_urls:
    print(file_item)
    quark.store(file_item['url'])
```
