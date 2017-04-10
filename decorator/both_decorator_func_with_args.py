# Both decorator and target function need arguments
def ver(v):
    # outer wrapper with 'f(target function)' as argument
    def wrapper(f):
        # inner wrapper with '*args' as arguments for target function
        def wrapper_f(*args):
            return "[{}] {}".format(v, f(*args))
        return wrapper_f
    return wrapper


@ver("1.1")
def say_hello(name):
    return "hello {}".format(name)


print(say_hello("Ted"))

