# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        dic = {}
        def go(root, depth, dic, parent):
            if root:
                #print(root.val, depth)
                dic[root.val] = (depth, parent)
                go(root.left, depth+1, dic, root.val)
                go(root.right, depth+1, dic, root.val)
        go(root, 0, dic, 0)
        return dic[x][0] == dic[y][0] and dic[x][1] != dic[y][1]


root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right = TreeNode(3)


s = Solution()
r = s.isCousins(root, 2,3)
print(r)

