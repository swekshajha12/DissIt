# https://leetcode.com/problems/path-sum-iii/description/?envType=study-plan-v2&envId=leetcode-75


from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def bruteForcePathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        result = 0

        def outerDfs(root):
            if not root:
                return
            innerDfs(root, 0)
            outerDfs(root.left)
            outerDfs(root.right)

        def innerDfs(root, current_sum):
            nonlocal result
            if not root:
                return
            current_sum = current_sum + root.val
            if current_sum == targetSum:
                result += 1
            innerDfs(root.left, current_sum)
            innerDfs(root.right, current_sum)

        outerDfs(root)
        return result

    def optimisedBruteForce(self, root, targetSum):
        def solve(root, currentSum):
            if not root:
                return 0
            count = 1 if currentSum + root.val == targetSum else 0

            # continue the path from the current node
            count += solve(root.left, currentSum + root.val)
            count += solve(root.right, currentSum + root.val)

            # start new paths from left and right children
            count += solve(root.left, 0)
            count += solve(root.right, 0)
            return count

        return solve(root, 0)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(root, targetSum):
            if not root:
                return 0

            res = 1 if root.val == targetSum else 0
            targetSum = targetSum - root.val
            res += dfs(root.left, targetSum)
            res += dfs(root.right, targetSum)
            return res

        return dfs(root, targetSum)


root = TreeNode(10)
root.left = TreeNode(5)
root.left.left = TreeNode(3)
root.right = TreeNode(-3)
root.right.right = TreeNode(11)

ob = Solution()
print(ob.bruteForcePathSum(root, 8))

