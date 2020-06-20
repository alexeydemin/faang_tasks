# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if root:
            if root.val == val:
                return root
            res = self.searchBST(root.left, val)
            if res:
                return res
            res1 = self.searchBST(root.right, val)
            if res1:
                return res1



# r = TreeNode(4)
# r.left = TreeNode(2)
# r.left.left = TreeNode(1)
# r.left.right = TreeNode(3)
# r.right = TreeNode(7)

r = TreeNode(18)
r.left = TreeNode(2)
r.right = TreeNode(22)
r.right.right = TreeNode(63)
r.right.right.right = TreeNode(84)

a = Solution().searchBST(r, 63)
print(a)
