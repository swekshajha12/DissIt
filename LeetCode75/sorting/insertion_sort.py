from typing import List


def insertion_sort(arr: List):
    for i in range(1, len(arr)):
        curr_ele = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > curr_ele:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_ele
    return arr


print(insertion_sort([3, 2, 4, 1]))
