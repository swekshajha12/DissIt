# https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        resDc = defaultdict(int)
        q = deque()
        q.append(root)
        level = 1

        while q:
            levelSum = 0
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    levelSum += node.val
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)
            resDc[level] = levelSum
            level += 1
        maxRes = float('-inf')
        minLevel = float('inf')
        for lev, val in resDc.items():
            if val > maxRes:
                maxRes = val
                minLevel = lev

        return minLevel


root = TreeNode(-100)
root.left = TreeNode(-200)
root.right = TreeNode(-300)
root.left.left = TreeNode(-20)
root.left.right = TreeNode(-5)
root.right.left = TreeNode(-10)

ob = Solution()
print(ob.maxLevelSum(root))
