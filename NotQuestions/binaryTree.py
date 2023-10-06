# create a binary tree
# all these traversals of the tree are dfs

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    @staticmethod
    def in_order_traversal( node):
        if node:
            TreeNode.in_order_traversal(node.left)
            print(node.value, end=' ')
            TreeNode.in_order_traversal(node.right)

    @staticmethod
    def pre_order_traversal(node):
        if node:
            print(node.value, end=' ')
            TreeNode.pre_order_traversal(node.left)
            TreeNode.pre_order_traversal(node.right)

    @staticmethod
    def post_order_traversal(node):
        if node:
            TreeNode.post_order_traversal(node.right)
            TreeNode.post_order_traversal(node.left)
            print(node.value, end=' ')



# create nodes
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# root.right.left = TreeNode(3)

TreeNode.in_order_traversal(root)
# TreeNode.pre_order_traversal(root)
# TreeNode.post_order_traversal(root)