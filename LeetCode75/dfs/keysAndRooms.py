# https://leetcode.com/problems/keys-and-rooms/description/?envType=study-plan-v2&envId=leetcode-75

from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = [0] * len(rooms)
        keys = set()

        def solve(i):
            if visited[i] == 1:
                return

            visited[i] = 1
            for key in rooms[i]:
                keys.add(key)
                solve(key)

        solve(0)
        print(visited)
        print(keys)
        if 0 in keys:
            keys.remove(0)

        return len(keys) == len(rooms) - 1


ob = Solution()
print(ob.canVisitAllRooms([[1], [3], [2], []]))
print(ob.canVisitAllRooms([[1, 3], [3, 0, 1, 2], [2], [0]]))
