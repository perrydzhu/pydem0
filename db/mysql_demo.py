from contextlib import contextmanager
import mysql.connector


class MySQLClient:
    def __init__(self, ):
        self.conn = mysql.connector.MySQLConnection()
        self.conf = {
            "user": "root",
            "password": "hello",
            "host": "127.0.0.1",
            "port": 3306,
            "database": "test",
        }

    @contextmanager
    def connect2mysql(self, **kwargs):
        print("connect to mysql")
        self.conn.connect(**kwargs)

        yield self.conn

        print("close mysql connection")
        self.conn.close()


if __name__ == "__main__":
    user = "jump3"
    sql = "SELECT 1 FROM demo2 WHERE name='{}'".format(user)
    ins_sql_tpl = "INSERT INTO demo2 VALUES (%s, %s)"
    # ins_sql_tpl = "INSERT INTO demo2(name, age) VALUES " \
    #               "(%(name)s, %(age)s)"

    print(type(ins_sql_tpl))

    cli = MySQLClient()
    with cli.connect2mysql(**cli.conf) as conn:
        cur = conn.cursor()
        cur.execute(sql)
        result = cur.fetchone()
        if result:
            print("user exists")
        else:
            print("user not exist, create")
            # data = {
            #     "name": user,
            #     "age": 100
            # }
            data = (user, 999)
            cur.execute(ins_sql_tpl, data)
            conn.commit()
