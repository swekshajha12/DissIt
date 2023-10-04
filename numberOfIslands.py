# https://leetcode.com/problems/number-of-islands/description/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        no_islands = 0
        rows, cols = len(grid), len(grid[0])
        if not grid:
            return 0

        def dfs(row, col):
            if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == "0":
                return

            # mark it as visited
            grid[row][col] = "0"

            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    no_islands += 1
        return no_islands


# Example usage:
grid = [
    ['1', '1', '0', '0', '0'],
    ['1', '1', '0', '0', '0'],
    ['0', '0', '1', '0', '0'],
    ['0', '0', '0', '1', '1']
]

ob = Solution()
result = ob.numIslands(grid)
print(result)  # Output: 3 (Three islands in the grid)
