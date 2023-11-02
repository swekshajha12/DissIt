def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        imin = i
        for j in range(i + 1, n):
            if arr[j] < arr[imin]:
                imin = j

        if imin != i:
            arr[imin], arr[i] = arr[i], arr[imin]

    return arr


print(selection_sort([3, 1, 2, 4]))
