import sqlite3

# 连接到数据库
conn = sqlite3.connect('files.db')
cursor = conn.cursor()

# 查询 file_name 和 share_link
cursor.execute('SELECT file_name, share_link FROM ALL_FILE')

# 处理查询结果
results = cursor.fetchall()
lines_to_write = '\n'.join([f'{row[0]}\\n{row[1]}' for row in results])  # 使用\\n作为文字字符分隔 file_name 和 share_link

# 关闭数据库连接
cursor.close()
conn.close()

# 追加到文件
with open('文件目录', 'a') as file:
    file.write(lines_to_write + '\n')  # 添加换行符以保持格式

print('数据已追加到文件。')
