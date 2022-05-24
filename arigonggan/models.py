import pymysql

conn = pymysql.connect(host='localhost', user='master', password='master', db='goorm', charset='utf8')

def usernser(infoQuery):
    cur = conn.cursor()
    sql = "insert into User (userId, password) VALUES (%s,%s)"
    cur.execute(sql,infoQuery)
    conn.commit()
    conn.close()