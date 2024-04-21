import sqlite3

# 连接到数据库文件（如果不存在，则创建一个新的）
conn = sqlite3.connect('files.db')

# 创建一个游标对象
c = conn.cursor()

# 创建 ALL_FILE 表
c.execute('''
CREATE TABLE ALL_FILE (
    FILE_ID TEXT PRIMARY KEY,
    FILE_NAME TEXT,
    FILE_TYPE TEXT,
    SHARE_LINK TEXT
)
''')

# 提交更改并关闭连接
conn.commit()
conn.close()
