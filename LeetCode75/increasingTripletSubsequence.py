# https://leetcode.com/problems/increasing-triplet-subsequence/description/?envType=study-plan-v2&envId=leetcode-75


'''
This is bullshit and would end up having O(n2) time complexity

# we'll use the logic used in product of array except itself
# here we'll maintain 2 arrays i.e left array and right product
# left array would contain true or false depening on if there's a
# smaller element on the left and similary for right array but
# checking if there are greater elements on the right
# then we'll multiply the two arrays and
# check the final array in sequence
# if they have 3 True present

'''

'''
Right approach

We'll use 2 pointer approach here

'''

from typing import List


class Solution:
    # good solution but time limit exceeded

    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        for i in range(1, len(nums) - 1):
            left = i - 1
            right = i + 1
            while left >= 0 and right <= len(nums) - 1:
                if nums[left] < nums[i]:
                    if nums[right] > nums[i]:
                        return True

                if nums[left] > nums[i]:
                    left -= 1

                if nums[right] < nums[i]:
                    right += 1

        return False

    def increasingTripletOptimised(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False

        min_num = float('inf')
        second_min_num = float('inf')

        for num in nums:
            if num <= min_num:
                min_num = num
            elif num <= second_min_num:
                second_min_num = num
            else:
                return True

        return False


ob = Solution()
print(ob.increasingTriplet([1, 2, 3, 4, 5]))
print(ob.increasingTriplet([5, 4, 3, 2, 1]))
print(ob.increasingTriplet([2, 1, 5, 0, 4, 6]))
