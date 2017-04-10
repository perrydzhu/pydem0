def attr(**kwargs):
    def wrapper(f):
        for k in kwargs:
            setattr(f, k, kwargs[k])
        return f
    return wrapper


@attr(version="1.0", author="Skipper")
def hello():
    print("say hello")


if __name__ == "__main__":
    print(hello.__name__)
    print(hello.__dict__)
    hello()
