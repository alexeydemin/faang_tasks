# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# Input: [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]

from typing import List


class Solution:
    def bstFromPreorder(self, pre: List[int]) -> TreeNode:
        arr = pre
        root = TreeNode(arr[0])
        i = 0
        found = False
        for i in range(1, len(arr)):
            if arr[0] < arr[i]:
                found = True
                break

        if not found:
            i += 1

        if len(arr[1:i]) > 1:
            root.left = self.bstFromPreorder(arr[1:i])
        elif len(arr[1:i]) == 1:
            root.left = TreeNode(arr[1:i][0])
        else:
            root.left = None

        if len(arr[i:]) > 1:
            root.right = self.bstFromPreorder(arr[i:])
        elif len(arr[i:]) == 1:
            root.right = TreeNode(arr[i:][0])
        else:
            root.right = None

        return root


s = Solution()
#res = s.bstFromPreorder([8,5,1,7,10,12]) #[8,5,10,1,7,null,12]
#res = s.bstFromPreorder([1])
res = s.bstFromPreorder([4,2]) #[4,2,null]
#res = s.bstFromPreorder([3, 1, 2]) #[3,1,null,null,2]
g = 1

# root = TreeNode(8)
# root.left = TreeNode(5)
# root.right = TreeNode(10)
# root.left.left = TreeNode(1)
# root.left.right = TreeNode(7)
# root.right.right = TreeNode(12)


root = TreeNode(3)
root.left = TreeNode(1)
root.left.right = TreeNode(2)


# Output: [8,5,10,1,7,null,12]

def printT(node):
    if not node:
        return
    if not node.left and not node.right:
        return
    print(node.left.val if node.left else None)
    print(node.right.val if node.right else None)

    printT(node.left)
    printT(node.right)


print(res.val)
printT(res)
# print(root.val)
# printT(root)
