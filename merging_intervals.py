"""

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

"""


# https://www.geeksforgeeks.org/merging-intervals/

class Solution:
    def merge_intervals(self, arr):
        if not arr:
            return []
        arr.sort()
        merged = [arr[0]]
        for i in range(1, len(arr)):
            current_start, current_end = arr[i]
            last_merged_start, last_merged_end = merged[-1]
            if current_start <= last_merged_end:
                merged[-1] = [last_merged_start, max(current_end, last_merged_end)]
            else:
                merged.append([current_start, current_end])

        return merged


ob = Solution()
print(ob.merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))
print(ob.merge_intervals([[1, 3], [1, 5], [2, 6], [8, 10], [15, 18], [2, 3]]))
