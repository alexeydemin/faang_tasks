# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
        return self.check(root, arr, 0)

    def check(self, root, arr, i):
        if not root or i == len(arr):
            return False

        if root.val == arr[i]:
            if not root.left and not root.right and i == len(arr) - 1:
                return True
            return self.check(root.left, arr, i + 1) or self.check(root.right, arr, i + 1)


root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.left.left = TreeNode(0)
root.left.right = TreeNode(1)
root.left.left.right = TreeNode(1)
root.left.right.left = TreeNode(0)
root.left.right.right = TreeNode(0)
root.right.left = TreeNode(0)

s = Solution()
r = s.isValidSequence(root, [0, 1, 0, 1])
print(r)
