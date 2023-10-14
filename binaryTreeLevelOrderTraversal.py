# https://leetcode.com/problems/binary-tree-level-order-traversal/description/

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            qlen = len(queue)
            for i in range(qlen):
                node = queue.popleft()
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)
            if level:
                res.append(level)
        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

ob = Solution()
print(ob.levelOrder(root))
