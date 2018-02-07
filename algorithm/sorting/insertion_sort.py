def insertion_sort(unsorted):
    n = len(unsorted)
    for i in range(1, n):       # range from 1 - 5
        tmp = unsorted[i]  # [7|2, 4 1, 5, 3], left: sorted, right: unsorted
        slot = i

        # use while loop to shift element greater than "tmp"
        while slot > 0 and unsorted[slot-1] > tmp:
            unsorted[slot] = unsorted[slot - 1]
            slot -= 1
        unsorted[slot] = tmp
        print(unsorted)
    return unsorted


if __name__ == '__main__':
    numbers = [7, 2, 4, 1, 5, 3]
    # numbers = [5, 4, 3, 2, 1, 0]
    sorted_list = insertion_sort(numbers)
    print(sorted_list)
