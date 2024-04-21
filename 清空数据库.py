import sqlite3

# 连接到SQLite数据库（如果不存在则创建）
conn = sqlite3.connect('files.db')

# 创建一个游标对象
cursor = conn.cursor()

# 列出数据库中的所有表
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()

# 遍历每个表并删除所有行
for table in tables:
    table_name = table[0]
    cursor.execute(f"DELETE FROM {table_name};")

# 提交更改并关闭连接
conn.commit()
conn.close()
