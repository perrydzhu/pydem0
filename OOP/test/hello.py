def say_hello(name):
    print("Hello %s" % name)
    print(__name__)


if __name__ == '__main__':
    say_hello("Ted")
