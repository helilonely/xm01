# -*- coding:utf-8 -*-
import pymysql





class GetDataByMySql(object):
    # self.db = pymysql.connect('192.168.76.41', 'root', 'root', 'User',charset="utf8")

    def bulid_conect(self):
        db = pymysql.connect(host='localhost', user='root', password='', database='test_1', charset="utf8")
        cursor = db.cursor()
        return (db,cursor)

    def query_sth(self, sqlstr):
        try:
            db, cursor = self.bulid_conect()
            cursor.execute(sqlstr)
            data = cursor.fetchall()
            print(data, type(data))
        finally:
            cursor.close()
            db.close()

        return data

    def excute_sql(self, sqlstr):
        db, cursor = self.bulid_conect()
        try:
            cursor.execute(sqlstr)
            db.commit()
        except Exception as e:
            print(e)
            db.rollback()
        finally:
            cursor.close()
            db.close()

if __name__ == '__main__':
    # DbConn().excute_sql(r"insert into t1(name) values('大')")
    result = GetDataByMySql().query_sth("select * from search")


