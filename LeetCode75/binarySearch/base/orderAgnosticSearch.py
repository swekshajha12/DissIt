class Solution:

    def asc_binary_search(self, arr, ele):
        left, right = 0, len(arr)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def desc_binary_search(self, arr, ele):
        left, right = 0, len(arr)
        while left <= right:
            mid = left + (right - left) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] < ele:
                right = mid - 1
            else:
                left = mid + 1
        return -1

    def search(self, arr, ele):
        n = len(arr)
        if arr[0] <= arr[n - 1]:
            return self.asc_binary_search(arr, ele)
        else:
            return self.desc_binary_search(arr, ele)


ob = Solution()
print(ob.search([1, 2, 3, 4, 5], 1))
print(ob.search([5, 4, 3, 2, 1], 1))
