# target function passed as a argument of decorator
def attr(f):
    # arguments of target function is passed here
    def wrapper(*args):
        print("[Greetings]")
        f(*args)
    return wrapper


@attr
def hello(name):
    print("Hello {}".format(name))


if __name__ == "__main__":
    hello("Ted")
