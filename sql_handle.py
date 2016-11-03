# coding: utf-8
'''
Created on 2016年9月7日

@author: Administrator
'''
import sqlite3


class sql_handle:
    def __init__(self, name):
        self.conn = sqlite3.connect('data/' + name + '.db')

    def create(self, sqls):
        self.conn.execute(sqls)
        print "Table created successfully"

    def into(self, values):
        cur = self.conn.cursor()
        cur.executemany('INSERT INTO data_url VALUES(?,?,?,?)', values)
        self.conn.commit()

    def selects(self, sqls, data):
        listdata = []
        if data == 1:
            cursor = self.conn.execute(sqls)
        else:
            cursor = self.conn.execute(sqls, (data,))
        for i in cursor:
            listdata.append(i)
        return listdata

    def read(self, sqls):
        listdata = []
        cursor = self.conn.execute(sqls)
        for row in cursor:
            listdata.append(row)
        return listdata

    def return_line(self, sqls):
        cursor = self.conn.execute(sqls)
        line = cursor.fetchone()
        return line[0]

    def updata(self, sqls, data):
        for i in data:
            self.conn.execute(sqls % i)
            self.conn.commit()

    def close(self):
        self.conn.close()


if __name__ == '__main__':
    sqls = '''CREATE TABLE data_url
       (id  integer primary key autoincrement ,
       url TEXT NOT NULL,
	url_re TEXT NOT NULL,
       state INT NOT NULL)
'''
    p1 = sql_handle('1')
    # p1.create(sqls)
    values = [
        (None, 'dsadas', 'dsada', 1),
        (None, 'dsadas', 'dsada', 1),
        (None, 'dsadas', 'dsada', 1),
    ]
    p1.into(values)
    print p1.selects('SELECT *  from data_url where state=1 LIMIT 10', 1)
    p1.close()
    '''
                常用sql
    SELECT *  from datas where state=1 LIMIT 10
    '''
