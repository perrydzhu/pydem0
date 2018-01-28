import random


def gen_rand_data(length=10):
    l = []
    data_range = 100

    for _ in range(length):
        l.append(random.randint(1, data_range))

    return l
