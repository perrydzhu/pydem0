# from __future__ import print_function


def print_multi_table():
    for i in range(1, 10):
        for j in range(1, i+1):
            # use from __future__
            # print("{} * {} = {}".format(i, j, i*j), end="")
            # print(" ", end="")

            print("{} * {} = {}".format(i, j, i*j)),
            print(" "),

        print("")

