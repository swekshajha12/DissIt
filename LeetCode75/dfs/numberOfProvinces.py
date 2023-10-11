# https://leetcode.com/problems/number-of-provinces/description/?envType=study-plan-v2&envId=leetcode-75

# This question is similar to  number of islands but quite different
# don't fall for the trap


from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        seen = set()

        def dfs(city):
            if city not in seen:
                seen.add(city)
                for j in range(len(isConnected)):
                    if isConnected[city][j] == 1:
                        dfs(j)

        cnt = 0
        for i in range(len(isConnected)):
            if i not in seen:
                dfs(i)
                cnt += 1
        return cnt

    def findNumberOfProvinces(self, isConnected):
        def dfs(city):
            visited[city] = True
            for neighbor in range(len(isConnected)):
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for city in range(n):
            if not visited[city]:
                provinces += 1
                dfs(city)

        return provinces


ob = Solution()
print(ob.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
print(ob.findCircleNum([[1, 0, 0], [0, 1, 0], [0, 0, 1]]))
print(ob.findCircleNum([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]))
