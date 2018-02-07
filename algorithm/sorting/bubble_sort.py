from utils import gen_rand_data


def bubble(data):
    print("origin: {}".format(data))
    length = len(data)

    while length > 0:
        for i in range(length-1):
            if data[i] > data[i+1]:
                tmp = data[i]
                data[i] = data[i+1]
                data[i+1] = tmp
            print("bubbling: {}".format(data))
        length -= 1
    return data


if __name__ == "__main__":
    l = gen_rand_data(10)
    print(bubble(l))

