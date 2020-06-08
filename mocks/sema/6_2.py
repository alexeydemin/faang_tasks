class Solution(object):
    def __init__(self):
        self.sm = 0

    def rangeSumBST(self, root, L, R):
        if root:
            self.rangeSumBST(root.left, L, R)
            self.rangeSumBST(root.right, L, R)
            if L <= root.val <= R:
                self.sm += root.val
        return self.sm