# inplace,
# space complexity: O(1)
# time complexity: worst case -> O(n2)
#                  best case -> O(n)

def bubble_sort(arr):
    n = len(arr)
    swaps = 0
    for i in range(n):
        for j in range(n - 1):
            if arr[j] > arr[j + 1]:
                swaps += 1
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

        if swaps == 0:
            return arr

    return arr


print(bubble_sort([3, 1, 2, 4]))
print(bubble_sort([1,2,3,4]))
