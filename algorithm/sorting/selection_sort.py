def selection_sort(unsorted):
    n = len(unsorted)

    for i in range(n - 1):
        min_index = i  # assume 1st element is minimum
        # scan to find the real minimum number
        for j in range(i + 1, n):
            if unsorted[j] < unsorted[min_index]:
                min_index = j

        tmp = unsorted[i]
        unsorted[i] = unsorted[min_index]
        unsorted[min_index] = tmp

    return unsorted


if __name__ == '__main__':
    # numbers = [4, 2, 5, 7, 1, 3]
    numbers = [7, 5, 4, 3, 2, 1]
    print(selection_sort(numbers))
