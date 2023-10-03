# https://leetcode.com/problems/equal-row-and-column-pairs/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        count = 0
        n = len(grid)
        for ri in range(n):
            for ci in range(n):
                if grid[ri] == [grid[i][ci] for i in range(n)]:
                    count += 1
        return count

    def countEqualRowColumnPairs(self, grid):
        n = len(grid)
        row_hash = {}
        count = 0

        # Calculate and store the hash values for each row.
        for ri in range(n):
            row_hash[tuple(grid[ri])] = row_hash.get(tuple(grid[ri]), 0) + 1

        # Check each column against the row hashes.
        for cj in range(n):
            col = [grid[ri][cj] for ri in range(n)]
            col_tuple = tuple(col)

            if col_tuple in row_hash:
                count += row_hash[col_tuple]

        return count


ob = Solution()
print(ob.equalPairs([[3, 2, 1], [1, 7, 6], [2, 7, 7]]))
print(ob.countEqualRowColumnPairs([[3, 1, 2, 2], [1, 4, 4, 5], [2, 4, 2, 2], [2, 4, 2, 2]]))
