def bubble_sort(unsorted):
    n = len(unsorted)
    for i in range(1, n):
        # print(range(n-i-1))
        for j in range(n-i):
            if unsorted[j] > unsorted[j+1]:
                tmp = unsorted[j]
                unsorted[j] = unsorted[j+1]
                unsorted[j+1] = tmp
        print(unsorted)

    return unsorted


if __name__ == '__main__':
    numbers = [2, 7, 4, 1, 5, 3]
    print(bubble_sort(numbers))