# https://leetcode.com/problems/asteroid-collision/description/?envType=study-plan-v2&envId=leetcode-75


from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stk = []
        for a in asteroids:
            while stk and stk[-1] > 0 > a:
                if stk[-1] < abs(a):
                    stk.pop()
                    continue
                elif stk[-1] == abs(a):
                    stk.pop()
                break
            else:
                stk.append(a)

        return stk


obj = Solution()
print(obj.asteroidCollision([5, 10, -5]))
print(obj.asteroidCollision([10, 2, -5]))
