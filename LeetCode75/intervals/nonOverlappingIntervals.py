# https://leetcode.com/problems/non-overlapping-intervals/description/?envType=study-plan-v2&envId=leetcode-75

# https://www.youtube.com/watch?v=0TYKyTwGOAs good explaination


from typing import List


class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count = 0
        if len(intervals) == 1:
            return 0
        prev_stpt, prev_enpt = intervals[0][0], intervals[0][1]
        for i in range(1, len(intervals)):
            curr_stpt, curr_enpt = intervals[i][0], intervals[i][1]
            if curr_stpt < prev_enpt:
                # there's an overlap
                # which one has more scope
                if prev_enpt >= curr_enpt:
                    prev_stpt, prev_enpt = curr_stpt, curr_enpt
                count += 1

            else:
                # no overlap, update the prev value
                prev_stpt, prev_enpt = curr_stpt, curr_enpt
        return count


ob = Solution()
print(ob.eraseOverlapIntervals([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(ob.eraseOverlapIntervals([[1, 2], [1, 2], [1, 2]]))
print(ob.eraseOverlapIntervals([[1, 2], [2, 3]]))
print(ob.eraseOverlapIntervals([[0, 2], [1, 3], [2, 4], [3, 5], [4, 6]]))
