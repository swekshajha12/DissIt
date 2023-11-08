# https://leetcode.com/problems/find-peak-element/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        left, right = 0, len(nums) - 1
        mid = (left + right) // 2

        while left <= right:
            if mid == len(nums) - 1:
                return mid
            if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
                return mid
            elif nums[mid] < nums[mid + 1]:
                left = mid + 1
            elif nums[mid] < nums[mid - 1]:
                right = mid - 1
            mid = (left + right) // 2

        return mid

    #  This solution will also work for when you when to find an element
    # where all elements to its left or right is smaller than that element
    def findPeakElementApp2(self, arr: List[int]) -> int:
        n = len(arr)
        mid = n // 2
        l = mid - 1
        r = mid + 1

        while l >= 0 and r < n:
            if arr[l] <= arr[mid] and arr[r] <= arr[mid]:
                l -= 1
                r += 1
            elif arr[l] > arr[mid] and arr[r] > arr[mid]:
                if arr[l] > arr[r]:
                    mid = l
                    l -= 1
                else:
                    mid = r
                    r += 1

            elif arr[l] > arr[mid]:
                mid = l
                l -= 1
            elif arr[r] > arr[mid]:
                mid = r
                r += 1
        if r >= n and l >= 0:
            if arr[l] > arr[mid]:
                mid = l

        elif r < n and l < 0:
            if arr[r] > arr[mid]:
                mid = r

        return mid


ob = Solution()
print(ob.findPeakElement([4, 2, 3, 1, 5]))
print(ob.findPeakElement([1, 2, 3, 1]))
print(ob.findPeakElement([1, 2, 1, 3, 5, 6, 4]))
print(ob.findPeakElement([1]))
print(ob.findPeakElement([1, 2, 3, 4, 5, 6]))
print(ob.findPeakElementApp2([1, 2, 3, 1]))
print(ob.findPeakElementApp2([1, 2, 1, 3, 5, 6, 4]))
print(ob.findPeakElementApp2([1]))
print(ob.findPeakElementApp2([1, 2, 3, 4, 5, 6]))
print(ob.findPeakElementApp2([2, 1]))
print(ob.findPeakElementApp2([1, 2]))
print(ob.findPeakElementApp2([6, 5, 4, 3, 2, 3, 2]))
