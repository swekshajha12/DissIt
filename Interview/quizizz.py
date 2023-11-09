def singleNumber(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        mid = (left + right) // 2

        # Check if mid is at an even index
        if mid % 2 == 1:
            mid -= 1

        # Compare the two adjacent elements
        if nums[mid] != nums[mid + 1]:
            right = mid
        else:
            left = mid + 2

    return nums[left]


# Example usage:
nums = [1, 1, 2, 2, 4]
# result = singleNumber(nums)
# print(singleNumber([3,3,7,7,10,11,11]))
print(singleNumber([2, 3, 3, 7, 7, 11, 11]))
# print(result)  # Output: 4
