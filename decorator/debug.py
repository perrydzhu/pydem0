def setup(host="localhost", port=6379, db=0):
    def wrapped(func):
        def new_func(*args, **kwargs):
            conn = "{}:{} - {}".format(host, port, db)
            return func(conn, *args, **kwargs)
        return new_func
    return wrapped


@setup("127.0.0.1", 8888, 4)
# @setup()
def do_sth(conn):
#def do_sth(conn, name):
    print(conn)
    # print(name)

# do_sth("Ted")
do_sth()
