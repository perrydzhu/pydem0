import random
import time
from datetime import datetime


def what_time_is_it():
    return datetime.now()


def doing_sth(tm, *args):
    for item in args:
        print("Do {}".format(item))
        print(tm())
        time.sleep(random.randint(1, 3))

if __name__ == "__main__":
    action = ["eating", "walking", "sleeping", "running"]
    doing_sth(what_time_is_it, *action)
