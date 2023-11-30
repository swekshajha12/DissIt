"""There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once
in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.



Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]

Output: 3


Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
"""

# https://leetcode.com/problems/gas-station/description/

from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        diff = []
        if n == 1:
            if gas[0] - cost[0] >= 0:
                return 0
            else:
                return -1
        for i in range(n):
            diff.append(gas[i] - cost[i])
        for i in range(n):
            j = (i + 1) % n
            res = diff[i]
            if res > 0:
                while j != i:
                    if res > 0:
                        res += diff[j]
                        j = (j + 1) % n
                    else:
                        break
                if j == i and res >= 0:
                    return i
        return -1

    def canCompleteCircuitBeaut(self, gas, cost):
        n = len(gas)
        diff = [gas[i] - cost[i] for i in range(n)]

        for i in range(n):
            if diff[i] >= 0:
                j = (i + 1) % n
                res = diff[i]

                while j != i and res > 0:
                    res += diff[j]
                    j = (j + 1) % n

                if j == i and res >= 0:
                    return i

        return -1

    def canCompleteCircuitOpt(self, gas, cost):
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i + 1
        return start


ob = Solution()
print(ob.canCompleteCircuitOpt([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
print(ob.canCompleteCircuitOpt([2, 3, 4], [3, 4, 3]))
print(ob.canCompleteCircuitOpt([4, 5, 3, 1, 4], [5, 4, 3, 4, 2]))
print(ob.canCompleteCircuitOpt([2], [2]))
