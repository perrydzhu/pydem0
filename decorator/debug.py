def setup(host="localhost", port=6379, db=0):
    def wrapped(func):
        conn = "{}:{} - {}".format(host, port, db)

        def new_func(*args):
            return func(conn, *args)

        return new_func

    return wrapped


@setup("127.0.0.1", 8877, 4)
# @setup()
def do_sth(*args):
    # def do_sth(conn, name):
    print(args)
    # print(name)


do_sth("Ted")
do_sth()
