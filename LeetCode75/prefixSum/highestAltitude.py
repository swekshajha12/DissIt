# https://leetcode.com/problems/find-the-highest-altitude/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = []
        res.append(0)
        res.append(gain[0])
        for i in range(1, len(gain)):
            res.append(gain[i] + res[i])
        # print(gain)
        # print(res)
        return max(res)

    def largestAltitudeApp2(self, gain):
        res = 0
        curr_alti = 0
        for i in range(len(gain)):
            curr_alti += gain[i]
            res = max(res, curr_alti)
        return res



obj = Solution()
print(obj.largestAltitude([-5, 1, 5, 0, -7]))
print(obj.largestAltitude([-4, -3, -2, -1, 4, 3, 2]))
print(obj.largestAltitudeApp2([-5, 1, 5, 0, -7]))
print(obj.largestAltitudeApp2([-4, -3, -2, -1, 4, 3, 2]))
