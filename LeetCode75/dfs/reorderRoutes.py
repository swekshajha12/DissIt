# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        count = 0
        visited = set()
        edges = {(a, b) for a, b in connections}
        neighbors = {city: [] for city in range(n)}

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)

        def dfs(city):
            nonlocal visited, edges, neighbors, count
            for neighbor in neighbors[city]:
                if neighbor in visited:
                    continue
                if (neighbor, city) not in edges:
                    count += 1
                visited.add(neighbor)
                dfs(neighbor)

        visited.add(0)
        dfs(0)
        return count


ob = Solution()
print(ob.minReorder(6, [[0,1],[1,3],[2,3],[4,0],[4,5]]))
print(ob.minReorder(5, [[1,0],[1,2],[3,2],[3,4]]))
print(ob.minReorder(3, [[1,0],[2,0]]))