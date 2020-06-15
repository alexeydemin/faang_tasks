from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        res = []

        def delete(node, to_delete):
            if node:
                lode = node
                if node.val in to_delete and node.left and node.right:
                    res.extend([node.left, node.right])
                    #del to_delete[node.val]
                    node = None
                delete(lode.left, to_delete)
                delete(lode.right, to_delete)


        delete(root, to_delete)

        if root.val not in to_delete:
            res.append(root)
        return res




root = TreeNode(1)
root.left = TreeNode(2)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
root.right.left = TreeNode(6)
root.right.right = TreeNode(7)

a = Solution().delNodes(root, [3,5])
b=1
