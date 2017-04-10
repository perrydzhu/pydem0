class MyDecorator(object):
    # target function passed in __init__()
    def __init__(self, f):
        print("inside myDecorator.__init__()")
        f()  # Prove that function definition has completed

    def __call__(self):
        print("inside myDecorator.__call__()")


@MyDecorator
def func():
    print("inside aFunction()")

print("Finished decorating aFunction()")

func()
