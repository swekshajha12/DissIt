# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List

# we first sort the points in ascending order, then we make a single array with all the points
# in order. After that we find the difference between the end and start of points and till the
# diff is strictly increasing, we consider it as one interval
"the above approach is too hacky, non optimised and doesn't work for all test cases"


# we'll do a diff approach as explained in https://www.youtube.com/watch?v=zfcGwzfDNu0

class Solution:
    def findMinArrowShotsBruteHackySol(self, points: List[List[int]]) -> int:
        points.sort()
        num_intervals = 1
        stk = []
        flat_list = [item for sublist in points for item in sublist]
        diff = [0]
        for i in range(1, len(flat_list) - 1, 2):
            diff.append(flat_list[i] - flat_list[i + 1])
        for ele in diff:
            if not stk:
                stk.append(ele)
            elif ele >= stk[-1] and ele > 0:
                stk.append(ele)
            elif ele == stk[-1] and ele == 0:
                stk.append(ele)
                num_intervals += 0.5
            else:
                stk.append(ele)
                num_intervals += 1
        if len(diff) >= 2 and len(diff) % 2 != 0:
            if diff[-1] < diff[-2]:
                num_intervals += 1

        return round(num_intervals)

    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        num_arrows = 1
        if len(points) == 1:
            return 1
        prev_stpt, prev_enpt = points[0][0], points[0][1]
        for i in range(1, len(points)):
            curr_stpt, curr_enpt = points[i][0], points[i][1]
            if curr_stpt <= prev_enpt:
                prev_stpt, prev_enpt = max(curr_stpt, prev_stpt), min(curr_enpt, prev_enpt)
            else:
                prev_stpt, prev_enpt = curr_stpt, curr_enpt
                num_arrows += 1
        return num_arrows


ob = Solution()
print(ob.findMinArrowShots([[1, 6], [2, 8], [7, 12], [10, 16]]))
print(ob.findMinArrowShots([[1, 2], [3, 4], [5, 6], [7, 8]]))
print(ob.findMinArrowShots([[1, 2], [2, 3], [3, 4], [4, 5]]))
print(ob.findMinArrowShots([[-2147483646, -2147483645], [2147483646, 2147483647]]))
