# https://leetcode.com/problems/binary-tree-right-side-view/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional, List
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        q = deque()
        q.append(root)

        while q:
            qlen = len(q)
            rightNode = q[-1]
            if rightNode:
                res.append(rightNode.val)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    if node.left:
                        q.append(node.left)
                    if node.right:
                        q.append(node.right)

        return res


root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.left.left = TreeNode(4)
root.right = TreeNode(5)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

root2 = TreeNode(1)
root2.left = TreeNode(2)

ob = Solution()
print(ob.rightSideView(root))
print(ob.rightSideView(root2))
