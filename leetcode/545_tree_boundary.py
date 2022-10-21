from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        def dfs_left(node):
            if not node or not node.left and not node.right:
                return
            boundary.append(node.val)
            if node.left:
                dfs_left(node.left)
            else:
                dfs_left(node.right)

        def dfs_right(node):
            if not node or not node.left and not node.right:
                return
            if node.right:
                dfs_right(node.right)
            else:
                dfs_right(node.left)
            boundary.append(node.val)

        def dfs_leaves(node):
            if not node:
                return
            dfs_leaves(node.left)
            if node != root and not node.left and not node.right:
                boundary.append(node.val)
            dfs_leaves(node.right)

        if not root:
            return []
        boundary = [root.val]
        dfs_left(root.left)
        dfs_leaves(root)
        dfs_right(root.right)
        return boundary


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5, TreeNode(7), TreeNode(8))),
                TreeNode(3, TreeNode(6, TreeNode(9), TreeNode(10))))
print(Solution.boundaryOfBinaryTree(None, root)) # [1, 2, 4, 7, 8, 9, 10, 6, 3]
