class Merge:
    def merge_sort(self, arr):
        n = len(arr)
        if n == 1:
            return arr
        arr1 = arr[:n // 2]
        arr2 = arr[(n // 2):]

        arr1 = self.merge_sort(arr1)
        arr2 = self.merge_sort(arr2)

        return self.merge_arr(arr1, arr2)

    def merge_arr(self, arr1, arr2):
        arr3 = []
        while arr1 and arr2:
            if arr1[0] > arr2[0]:
                arr3.append(arr2[0])
                arr2.pop(0)
            else:
                arr3.append(arr1[0])
                arr1.pop(0)

        if arr1:
            while arr1:
                arr3.append(arr1[0])
                arr1.pop(0)

        if arr2:
            while arr2:
                arr3.append(arr2[0])
                arr2.pop(0)

        return arr3


ob = Merge()
print(ob.merge_sort([3,2,4,1]))