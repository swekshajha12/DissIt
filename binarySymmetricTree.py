# https://leetcode.com/problems/symmetric-tree/description/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkSymmetry(self, p: Optional[TreeNode], q: Optional[TreeNode]):
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.checkSymmetry(p.left, q.right) and self.checkSymmetry(p.right, q.left)

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.checkSymmetry(root.left, root.right)


root = TreeNode(1)
root.left = TreeNode(2)
# root.left.left = TreeNode(3)
root.left.right = TreeNode(3)

root.right = TreeNode(2)
# root.right.left = TreeNode(5)
root.right.right = TreeNode(3)

ob = Solution()
print(ob.isSymmetric(root))

# This won't work, lets try the same approach we did when checking if 2 binary trees were same
# class Solution:
#     def postOrderTraversal(self, root):
#         res = []
#         def solve(root):
#             if root:
#                 solve(root.right)
#                 solve(root.left)
#                 res.append(root.val)
#         solve(root)
#         return res
#
#     def diffOrderTraversal(self, root):
#         res = []
#         def solve(root):
#             if root:
#                 solve(root.left)
#                 solve(root.right)
#                 res.append(root.val)
#         solve(root)
#         return res
#
#     def isSymmetric(self, root: Optional[TreeNode]) -> bool:
#         left_res, right_res = self.diffOrderTraversal(root.left), self.postOrderTraversal(root.right)
#         print(left_res)
#         print(right_res)
#         if left_res == right_res:
#             return True
#         return False
