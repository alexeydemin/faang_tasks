# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.res = 0

    def util(self, node):
        if not node:
            return 0

        l = self.util(node.left)
        r = self.util(node.right)
        max_val = max(l + node.val, r + node.val, node.val)
        max_top = max(max_val, r + l + node.val)
        self.res = max(self.res, max_top)

        return max_val

    def maxPathSum(self, root: TreeNode) -> int:
        self.res = float('-inf')
        self.util(root)
        return self.res


root = TreeNode(10)
root.left = TreeNode(2)
root.right = TreeNode(10)
root.left.left = TreeNode(20)
root.left.right = TreeNode(1)
root.right.right = TreeNode(-25)
root.right.right.left = TreeNode(3)
root.right.right.right = TreeNode(4)

s = Solution()
r = s.maxPathSum(root)

print(r)
