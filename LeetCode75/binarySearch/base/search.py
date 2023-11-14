# Given a sorted array arr[] of n elements, write a function to search a given element x in arr[].

class Solution:
    def search(self, arr, ele):
        left, right = 0, len(arr)
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == ele:
                return mid
            elif arr[mid] < ele:
                left = mid + 1
            else:
                right = mid - 1

        return -1


ob = Solution()
print(ob.search([1, 2, 3, 4, 5], 2))
