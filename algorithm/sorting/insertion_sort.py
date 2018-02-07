def insertion_sort(unsorted_list):
    n = len(unsorted_list)
    for i in range(1, n):       # range from 1 - 5
        tmp = unsorted_list[i]  # [7|2, 4 1, 5, 3], left: sorted, right: unsorted
        slot = i

        # use while loop to shift element greater than "tmp"
        while slot > 0 and unsorted_list[slot-1] > tmp:
            unsorted_list[slot] = unsorted_list[slot-1]
            slot -= 1
        unsorted_list[slot] = tmp
        print(unsorted_list)
    return unsorted_list


if __name__ == '__main__':
    numbers = [7, 2, 4, 1, 5, 3]
    # numbers = [5, 4, 3, 2, 1, 0]
    sorted_list = insertion_sort(numbers)
    print(sorted_list)
