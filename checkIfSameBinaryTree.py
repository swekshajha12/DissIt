# https://leetcode.com/problems/same-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        # if both the nodes are empty, they are equal
        if not p and not q:
            return True

        # if one of the nodes is empty, they are not equal
        if not p or not q:
            return False

        # if value of the nodes don't match, they are unequal
        if p.val != q.val:
            return False

        # recursively check for each side now
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


p = TreeNode(1)
p.left = TreeNode(1)
# p.right = TreeNode(3)

q = TreeNode(1)
# q.left = TreeNode(2)
q.right = TreeNode(1)
# q.right.left = TreeNode(4)

ob = Solution()
print(ob.isSameTree(p, q))
