import time
from threading import Thread


def hello():
    print("say hello in 5s")
    time.sleep(5)
    print("HELLO")


if __name__ == "__main__":
    print("start thread")
    t = Thread(name="robot", target=hello)
    t.start()
    # t.join()
    print("main end")


