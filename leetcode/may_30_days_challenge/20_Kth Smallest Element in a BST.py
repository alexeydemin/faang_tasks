# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        for i, a in enumerate(self.gen(root)):
            if i + 1 == k:
                return a

    def gen(self, node):
        if node:
            yield from self.gen(node.left)
            yield (node.val)
            yield from self.gen(node.right)


# root = [3,1,4,null,2], k = 1, OUTPUT = 1
# root = TreeNode(3)
# root.left = TreeNode(1)
# root.left.right = TreeNode(2)
# root.right = TreeNode(4)


# root = [5,3,6,2,4,null,null,1], k = 3, OUTPUT = 3
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(6)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.left.left.left = TreeNode(1)

s = Solution()
print(s.kthSmallest(root, 3))
# print(s.kthSmallest(root, 1))  #1
