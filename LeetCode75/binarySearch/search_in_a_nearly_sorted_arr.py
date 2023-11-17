class solution:
    def search(self, arr, target):
        n = len(arr)
        left, right = 0, n - 1
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == target:
                return mid
            if mid != n - 1 and arr[mid + 1] == target:
                return mid + 1
            if mid != 0 and arr[mid - 1] == target:
                return mid - 1
            elif arr[mid] < target:
                left = mid + 2
            elif arr[mid] > target:
                right = mid - 2

        return mid

ob = solution()
print(ob.search([2,3,10,4,40], 4))
