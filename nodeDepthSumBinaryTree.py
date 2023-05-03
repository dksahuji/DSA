def nodeDepths(root, level=0):
    if root is None:
        return 0
    return level + nodeDepths(root.left, level + 1) + nodeDepths(root.right, level + 1)

def nodeDepths(root, level=1):
    if root is None:
        return 0
    if root.left != None:
        left = level + nodeDepths(root.left, level + 1)
    else:
        left = 0
    if root.right != None:
        right= level + nodeDepths(root.right, level + 1)
    else:
        right = 0
    return left + right


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


