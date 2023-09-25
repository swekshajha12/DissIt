from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root: Optional[TreeNode]) -> int:
    # Base case: If the tree is empty, its depth is 0.
    if not root:
        return 0

    # Recursively calculate the depth of the left and right subtrees.
    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    # The depth of the tree is the maximum depth of its left and right subtrees,
    # plus 1 to account for the root node.
    return max(left_depth, right_depth) + 1


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.right.right = TreeNode(3)

print(maxDepth(root))