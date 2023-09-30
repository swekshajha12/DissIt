# https://leetcode.com/problems/product-of-array-except-self/description/?envType=study-plan-v2&envId=leetcode-75

# We'll find the left product and right product for each index and then
# multiply the left product and right product to get the solution


from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = []
        left_prod = [1] * len(nums)
        right_prod = [1] * len(nums)

        # calculate left product
        left = 1
        for i in range(1, n):
            left *= nums[i - 1]
            left_prod[i] = left

        # calculate the right product
        right = 1
        for i in range(n - 2, -1, -1):
            right *= nums[i + 1]
            right_prod[i] = right

        for i in range(n):
            res.append(left_prod[i] * right_prod[i])

        return res


ob = Solution()
print(ob.productExceptSelf([1, 2, 3, 4]))
print(ob.productExceptSelf([-1, 1, 0, -3, 3]))
