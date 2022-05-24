import pymysql

conn = pymysql.connect(host='localhost', user='root', password='lim1231', db='goorm', charset='utf8')

def usernser(infoQuery):
    cur = conn.cursor()
    sql = "insert into user (userId, password) VALUES (%s,%s)"
    cur.execute(sql,infoQuery)
    conn.commit()
    conn.close()