class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorder(root):
    if root:
        inorder(root.left)
        print(root.val)
        inorder(root.right)

def preorder(root):
    if root:
        print(root.val)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.val)


def bfs(root):
    if root:
        q = [root]
        while q:
            node = q.pop(0)
            print(node.val)

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)


root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
# inorder(root)
# print('==')
# preorder(root)
# print('==')
# postorder(root)

print('============')
bfs(root)
