# https://leetcode.com/problems/count-good-nodes-in-binary-tree/?envType=study-plan-v2&envId=leetcode-75


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if not root.left and not root.right:
            return 1

        def solve(root, maxVal):
            if not root:
                return 0

            if root:
                res = 1 if root.val >= maxVal else 0
                maxVal = max(maxVal, root.val)

                res += solve(root.left, maxVal)
                res += solve(root.right, maxVal)
                return res

        return solve(root, root.val)


root = TreeNode(2)
root.right = TreeNode(4)
root.right.left = TreeNode(10)
root.right.right = TreeNode(8)
root.right.right.left = TreeNode(4)

ob = Solution()
print(ob.goodNodes(root))
