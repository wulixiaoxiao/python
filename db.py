import mysql.connector
class db(object):
    def __init__(self):
        try:
            conn = mysql.connector.connect(user='root', password='root', database='test')
            self.__conn = conn
        except Exception as e:
            print(e)
            exit()
    def getConn(self):
        return self.__conn

    def select(self, tab, where='', columns=[], limit=10):
        cols = ",".join(str(i) for i in columns)
        if cols == '':
            cols = "*"
        if where == '':
            where = 1
        if limit != '':
            limit = 10
        sql = 'select %s from %s where %s limit %s' % (cols, str(tab), where, limit)
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            results = cursor.fetchall()
            cursor.close()
            return results
        except Exception as e:
            print(e)
        finally:
            self.__conn.close()


    def insert(self, tab, data={}):
        if len(data) <= 0:
            return False
        sql = "insert into " + tab
        sql += ' ('
        sql += ",".join("`"+str(i)+"`" for i in data.keys())
        sql += ") "
        sql += ' values ('
        sql += ",".join("'" + str(i) + "'" for i in data.values())
        sql += ")"
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            self.__conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            self.__conn.rollback()
            return False
        finally:
            self.__conn.close()
            return False

    def update(self, tab, where, data={}):
        if len(data) <= 0:
            return False
        sql = "update " + tab
        sql += ' set '
        sql += ",".join("`"+str(k)+"`='"+str(v)+"'" for k,v in data.items())
        sql += " where " + where
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            self.__conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            self.__conn.rollback()
        finally:
            self.__conn.close()
            return False

    def delete(self, tab, where):
        if where == '':
            return False
        sql = "delete from %s where %s" % (tab, where)
        try:
            cursor = self.__conn.cursor()
            cursor.execute(sql)
            self.__conn.commit()
            cursor.close()
            return True
        except Exception as e:
            print(e)
            self.__conn.rollback()
        finally:
            self.__conn.close()
            return False
