import pymysql

# connect to db
# docker: 172.17.0.1
conn = pymysql.connect("172.17.0.1", "daihao", "dh123456", "flask")

# cursor
cursor = conn.cursor()

# sql
sql = "select * from test"

# execute
try:
    cursor.execute(sql)
    results = cursor.fetchall()
    print(results)
except:
    print("Error: unable to fetch data")


conn.close()