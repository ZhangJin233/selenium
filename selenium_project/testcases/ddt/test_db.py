import pytest
import pymysql 
pymysql.install_as_MySQLdb()


dbconn = pymysql.connect(
    user='root', 
    password='12345678',
    host='localhost',
    port=3306,
    database='test_db'
)

def get_data():
    query_sql = 'select * from user'
    lst = []
    cursor = dbconn.cursor()
    cursor.execute(query_sql)
    data = cursor.fetchall()
    print (data)
    dbconn.close()
    # try:
    #     cursor = dbconn.cursor()
    #     cursor.execute(query_sql)
    #     r = cursor.fetchall()
    #     for x in r:
    #         u = (x[0], x[1], x[2])
    #         lst.append(u)
    #     return lst
    # finally:
    #     cursor.close()
    #     dbconn.close()

# @pytest.mark.parametrize('id, name, pwd', get_data())
# def test1(id, name, pwd):
#     print(id, name, pwd)


if __name__ == '__main__':
    # pytest.main(['-sv'])
    get_data()


