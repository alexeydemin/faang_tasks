from typing import List
from collections import deque


class TreeNode:
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right
        self.par = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def dfs(node, par=None):
            if node:
                node.par = par
                dfs(node.right, node)
                dfs(node.left, node)

        dfs(root)

        q = deque()
        q.append((target, 0))
        seen = {target}
        while q:
            if q[0][1] == k:
                return [node.val for node, d in q]
            node, d = q.popleft()
            for member in [node.par, node.left, node.right]:
                if member and member not in seen:
                    seen.add(node)
                    q.append((member, d+1))
        return []


# root = [3, 5, 1, 6, 2, 0, 8, null, null, 7, 4], target = 5, k = 2
target = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)))
root = TreeNode(3, target, TreeNode(1, TreeNode(0), TreeNode(8)))

print(Solution.distanceK(None, root, target, 2))
