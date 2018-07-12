import pymysql


name = raw_input()
# connect to db
# docker: 172.17.0.1
conn = pymysql.connect("172.17.0.1", "daihao", "123456", "flask")

# cursor
cursor = conn.cursor()
# sql
sql = "select * from test"
sql_ins = "insert into test (name) values ('%s')" %(name)

try:
    cursor.execute(sql_ins)
    conn.commit()
except:
    conn.rollback()

# execute
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
except:
    print("Error: unable to fetch data")


conn.close()