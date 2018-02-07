def selection_sort(unsorted):
    n = len(unsorted)
    for i in range(n - 1):
        min_no = i

        # scan to find the minimum number
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_no]:
                min_no = j
        tmp = unsorted[i]
        unsorted[i] = unsorted[min_no]
        unsorted[min_no] = tmp
    return unsorted


if __name__ == '__main__':
    numbers = [4, 2, 5, 7, 1, 3]
    print(selection_sort(numbers))
