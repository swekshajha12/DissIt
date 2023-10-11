# https://leetcode.com/problems/number-of-recent-calls/description/?envType=study-plan-v2&envId=leetcode-75
from collections import deque


class RecentCounter:

    def __init__(self):
        self.queue = deque()

    def ping(self, t: int) -> int:
        while self.queue and self.queue[0] < t - 3000:
            self.queue.popleft()

        self.queue.append(t)
        return len(self.queue)


# Example usage:
recentCounter = RecentCounter()
print(recentCounter.ping(1))  # Output: 1
print(recentCounter.ping(100))  # Output: 2
print(recentCounter.ping(3001))  # Output: 3
print(recentCounter.ping(3002))
