import random

a = True
num_sorts = 0


def is_sorted(ls):
    return ls == sorted(ls)


def shellSort(items):
    gap = len(items) // 3
    while gap > 0:
        for start in range(gap):
            insertionSort(items, start, gap)
        print("After increment of size", gap,
              "the list is", items)
        gap //= 3


def insertionSort(items, start, gap):
    global num_sorts
    for i in range(start + gap, len(items), gap):
        m = items[i]
        while i >= gap and items[i - gap] > m:
            items[i] = items[i - gap]
            i = i - gap
        items[i] = m
        num_sorts += 1


# insertion sort (by me, Doltum)
def insertion_sort(ls):
    global num_sorts
    for index, element in enumerate(ls[1:]):
        index += 1
        while index >= 0:
            if index == 0 or ls[index - 1] < element:
                ls[index] = element
                num_sorts += 1
                print(ls)
                break
            else:
                ls[index] = ls[index - 1]

            index -= 1
    print("Insertion sort did", num_sorts, "sorts")
    num_sorts = 0


def shell_sort(ls, initial_gap=3, gap_decrement=2, debug=False):
    for gap_val in range(initial_gap, 1, -gap_decrement):
        for remainder in range(len(ls) // gap_val):
            shell_ls = ls[remainder::initial_gap]

            if debug:
                print('unsorted', shell_ls)

            insertion_sort(shell_ls)

            if debug:
                print('sorted', shell_ls)

            ls[remainder::initial_gap] = shell_ls

            if debug:
                print('actual_list', ls)

    print('gapped', ls)
    insertion_sort(ls)


quicksort_count = 0


def quick_sort(ls, first, last):
    if first < last:
        split_point = partition(ls, first, last)
        quick_sort(ls, first, split_point - 1)
        quick_sort(ls, split_point + 1, last)


def partition(ls, first, last):
    global quicksort_count
    pivot_value = ls[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and ls[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while ls[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            if not right_mark == left_mark:
                quicksort_count += 1
            ls[left_mark], ls[right_mark] = ls[right_mark], ls[left_mark]
    if not right_mark == left_mark:
        quicksort_count += 1
    ls[first], ls[right_mark] = ls[right_mark], ls[first]
    print(quicksort_count)
    return right_mark


def merge_sort(ls):
    if len(ls) <= 1:
        return

    split_index = len(ls) // 2
    left_ls = ls[:split_index]
    right_ls = ls[split_index:]

    merge_sort(left_ls)
    merge_sort(right_ls)
    raise Exception


merge_count = 0


def mergeSort(ls):
    global merge_count
    print("Splitting ", ls)
    if len(ls) > 1:
        mid = len(ls) // 2
        left_ls = ls[:mid]
        right_ls = ls[mid:]
        mergeSort(left_ls)
        mergeSort(right_ls)

        print("Merging ", ls)
        left_e_index, right_e_index, next_sort_index = 0, 0, 0

        left_len, right_len = len(left_ls), len(right_ls)
        while left_e_index < left_len and right_e_index < right_len:
            if left_ls[left_e_index] <= right_ls[right_e_index]:
                merge_count += 1
                print('merge sort swap', ls[next_sort_index], right_ls[left_e_index])
                ls[next_sort_index] = left_ls[left_e_index]
                left_e_index += 1
            else:
                merge_count += 1
                print('merge sort swap', ls[next_sort_index], right_ls[right_e_index])
                ls[next_sort_index] = right_ls[right_e_index]
                right_e_index += 1
            next_sort_index += 1
        while left_e_index < left_len:
            merge_count += 1
            print('merge sort swap', ls[next_sort_index], right_ls[left_e_index])
            ls[next_sort_index] = left_ls[left_e_index]
            left_e_index, next_sort_index = left_e_index + 1, next_sort_index + 1

        while right_e_index < right_len:
            merge_count += 1
            print('merge sort swap', ls[next_sort_index], right_ls[right_e_index])
            ls[next_sort_index] = right_ls[right_e_index]
            right_e_index, next_sort_index = right_e_index + 1, next_sort_index + 1


# counting sort for digits 0 - 9
def count_sort(arr, pos, m):
    # count the same digits and put their counts at index = digit
    counts = [0 for _ in range(11)]
    for i in arr:
        i = str(i)
        while len(i) < m:  # add 0s in front of small numbers
            i = '0' + i
        i = int(i[pos])
        counts[i] += 1
    # convert counts into ranking: each index value = (number of items <= i)
    for i in range(10):
        counts[i] += counts[i - 1]

    output = [0 for _ in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr) - 1, -1, -1):
        j = str(arr[i])
        while len(j) < m:
            j = '0' + j
        j = int(j[pos])
        output[counts[j] - 1] = arr[i]
        counts[j] -= 1

    return output


def radix_sort(arr, pos):
    for i in range(pos - 1, -1, -1):
        arr = count_sort(arr, i, pos)
    return arr


def countSort(arr):
    # count the same digits and put their counts at index = digit
    counts = [0 for _ in range(11)]
    for i in arr:
        counts[i] += 1
    # convert counts into ranking: each index value = (number of items <= i)
    for i in range(10):
        counts[i] += counts[i - 1]
    print(counts, len(counts))
    output = [0 for _ in range(len(arr))]
    # use ranking as index and index as values
    for i in range(len(arr) - 1, -1, -1):
        print(i, arr[i], counts[arr[i]])
        output[counts[arr[i]] - 1] = arr[i]
        counts[arr[i]] -= 1

    return output


merge_sort_count = 0


def mergeSort(items):
    global merge_sort_count
    merge_sort_count += 1
    print("Splitting ", items)
    if len(items) > 1:
        mid = len(items) // 2
        l = items[:mid]
        r = items[mid:]
        mergeSort(l)
        mergeSort(r)
        print("Merging ", items)
        left_ls_ind, right_ls_ind, to_swap_index = 0, 0, 0
        while left_ls_ind < len(l) and right_ls_ind < len(r):
            if l[left_ls_ind] <= r[right_ls_ind]:
                items[to_swap_index] = l[left_ls_ind]
                left_ls_ind += 1
            else:
                items[to_swap_index] = r[right_ls_ind]
                right_ls_ind += 1
            to_swap_index += 1
        while left_ls_ind < len(l):
            items[to_swap_index] = l[left_ls_ind]
            left_ls_ind, to_swap_index = left_ls_ind + 1, to_swap_index + 1
        while right_ls_ind < len(r):
            items[to_swap_index] = r[right_ls_ind]
            right_ls_ind, to_swap_index = right_ls_ind + 1, to_swap_index + 1


list_ = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(list_)
print(list_)
print(merge_sort_count)
