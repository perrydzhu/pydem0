def connect2redis(host="localhost", port=6379, db=0):
    def wrapper1(f):
        def wrapper2(*args, **kwargs):
            redis_conn = "{}:{}  {}".format(host, port, db)
            f(*args, **kwargs)
        return wrapper2
    return wrapper1

def ver(v):
    # outer wrapper with 'f(target function)' as argument
    def wrapper(f):
        # inner wrapper with '*args' as arguments for target function
        def wrapper_f(*args):
            return "[{}] {}".format(v, f(*args))
        return wrapper_f
    return wrapper


@connect2redis("127.0.0.1", 8888, 0)
def say_hello(name):
    return "hello {}".format(name)


print(say_hello("Ted"))
