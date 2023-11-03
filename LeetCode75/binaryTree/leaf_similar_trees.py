# https://leetcode.com/problems/leaf-similar-trees/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def preOrderTraversal(self, root: Optional[TreeNode]) -> list:
        res = []

        def solve(root):
            if root:
                if not root.left and not root.right:
                    res.append(root.val)
                solve(root.left)
                solve(root.right)

        solve(root)
        return res

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leafNodesTree1 = self.preOrderTraversal(root1)
        leafNodesTree2 = self.preOrderTraversal(root2)

        print(leafNodesTree1)
        print(leafNodesTree2)

        if leafNodesTree1 == leafNodesTree2:
            return True
        else:
            return False


root1 = TreeNode(1)
root1.left = TreeNode(3)
root1.right = TreeNode(3)

root2 = TreeNode(2)
root2.left = TreeNode(2)
root2.right = TreeNode(3)

ob = Solution()
print(ob.leafSimilar(root1, root2))
