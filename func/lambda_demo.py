
def sayhi(name):
    print("hi {}".format(name))

f = lambda x: sayhi(x)

f("hello")
