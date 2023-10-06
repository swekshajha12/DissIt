# https://leetcode.com/problems/search-in-a-binary-search-tree/description/?envType=study-plan-v2&envId=leetcode-75

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    # def traverseTree(self, root):
    #     res = []
    #
    #     def solve(root):
    #         if root:
    #             res.append(root.val)
    #             solve(root.left)
    #             solve(root.right)
    #     solve(root)
    #     return res

    def findRoot(self, root, val):
        res = []

        def solve(root, val):
            if root:
                if root.val > val:
                    solve(root.left, val)
                elif root.val < val:
                    solve(root.right, val)
                else:
                    res.append(root)
                    return

        solve(root, val)
        if res:
            return res[0]
        else:
            return None

    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        node = self.findRoot(root, val)
        if node:
            return node
        else:
            return None


root = TreeNode(10)
root.left = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right = TreeNode(12)

ob = Solution()
print(ob.searchBST(root, 6))
print(ob.searchBST(root, 2))
