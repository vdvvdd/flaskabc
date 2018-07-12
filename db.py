import pymysql

# connect to db
# docker: 172.17.0.1
conn = pymysql.connect("172.17.0.1", "daihao", "123456", "flask")

# cursor
cursor = conn.cursor()


def add_user(username, passowrd):
    sql = "insert into users (username, password) values ('%s', '%s')" %(username, password)

    try:
        cursor.execute(sql)
        conn.commit()
    except:
        print("insert error")
        conn.rollback()

    conn.close()

# # sql
# sql = "select * from test"
# sql_ins = "insert into test (name) values ('%s')" %(name)

# try:
#     cursor.execute(sql_ins)
#     conn.commit()
# except:
#     conn.rollback()

# # execute
# try:
#     cursor.execute(sql)
#     results = cursor.fetchall()
#     print(results)
# except:
#     print("Error: unable to fetch data")


# conn.close()