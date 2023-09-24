# https://leetcode.com/problems/binary-tree-inorder-traversal/
# recursive solution

from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def solve(root):
            if root:
                solve(root.left)
                res.append(root.val)
                solve(root.right)

        solve(root)
        return res


# Create the binary tree from the given input [1,null,2,3]
root = TreeNode(1)
root.right = TreeNode(2)
root.right.left = TreeNode(3)

# Call the inorderTraversal function on the root
ob = Solution()
result = ob.inorderTraversal(root)
print(result)
