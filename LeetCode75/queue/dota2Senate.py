# https://leetcode.com/problems/dota2-senate/?envType=study-plan-v2&envId=leetcode-75

# we need to use 2 queues for this question

from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiantQueue = deque()
        direQueue = deque()
        for i in range(len(senate)):
            if senate[i] == 'R':
                radiantQueue.append(i)
            else:
                direQueue.append(i)

        while radiantQueue and direQueue:
            rad, dire = radiantQueue.popleft(), direQueue.popleft()
            if rad < dire:
                radiantQueue.append(rad + n)
            else:
                direQueue.append(dire + n)

        if radiantQueue:
            return 'Radiant'
        else:
            return 'Dire'


ob = Solution()
print(ob.predictPartyVictory("RD"))
print(ob.predictPartyVictory("RDDR"))
