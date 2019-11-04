# from pymysql import cursors, connect
#
# # 连接数据库
# conn = connect(host='127.0.0.1',
#                user='root',
#                password='root',
#                db='guest',
#                charset='utf8mb4',
#                cursorclass=cursors.DictCursor)
#
# try:
#     with conn.cursor() as cursor:
#     sql = 'INSERT INTO sign_guest (realname, phone, email, sign, event_id, create_time)' \
#           'VALUE ("tom", 1888888888, "tom@163", 0, 1, NOW());'
#     cursor.execute(sql)
#     # 提交事务
#     conn.commit()
#
#     with conn.cursor() as cursor:
#         sql = "SELECT realname, phone, email, sign FROM sign_guest WHERE phone=%s"
#         cursor.execute(sql, ('1888888888',))
#         result = cursor.fetchone()
#         print(result)
# finally:
#     conn.close()
