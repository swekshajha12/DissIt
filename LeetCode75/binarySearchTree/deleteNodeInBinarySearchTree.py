# https://leetcode.com/problems/delete-node-in-a-bst/?envType=study-plan-v2&envId=leetcode-75


# didn't understand shit in this question, reattempt later

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root
        if key > root.val:
            root.right = self.deleteNode(root.right)
        elif key < root.val:
            root.left = self.deleteNode(root.left)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left

            # find the min from the right sub tree
            curr = root.right
            while curr.left:
                curr = curr.left
            root.val = curr.val
            root.right = self.deleteNode(root.right, root.val)
        return root
