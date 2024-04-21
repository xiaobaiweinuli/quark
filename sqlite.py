import sqlite3


# 创建内存数据库

class SqlLiteOperator:
    def __init__(self):
        self.conn = sqlite3.connect('files.db')
        self.create_table()

    def create_table(self):
        """创建文件检索表"""
        c = self.conn.cursor()
        c.execute('CREATE TABLE IF NOT EXISTS ALL_FILE (FILE_ID TEXT PRIMARY KEY, FILE_NAME TEXT NOT NULL, FILE_TYPE TEXT, SHARE_LINK TEXT);')
        self.conn.commit()

    def fetch_files(self, file_name) -> bool:
        """检索文件,如果已存在那么返回False"""
        c = self.conn.cursor()
        c.execute('SELECT FILE_NAME FROM ALL_FILE WHERE FILE_NAME =?', (file_name,))
        files = c.fetchall()
        if files:
            return False
        return True

    def insert_files(self, file_id, file_name, file_type, share_link):
        """插入文件"""
        c = self.conn.cursor()
        c.execute("INSERT INTO ALL_FILE (FILE_NAME, SHARE_LINK) VALUES (?,?)", (file_name, share_link))
        self.conn.commit()

    def update_files(self, file_name, share_link):
        c = self.conn.cursor()
        c.execute("UPDATE ALL_FILE SET SHARE_LINK=? WHERE FILE_NAME=?", (share_link, file_name))
        self.conn.commit()

    def __del__(self):
        self.conn.close()
