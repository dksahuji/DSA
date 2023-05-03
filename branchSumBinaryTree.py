
'''
tree =   1
       /  \
      2     3
     / \   / \
    4   5 6   7
   / \ / 
  8  9 10
output = [15, 16, 18, 10, 11]
'''
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def DFS(root, val, l):
    if root is None:
        return
    
    val += root.value
    if ( root.left==None) and ( root.right==None):
        l.append(val)
        return
    
    DFS(root.left, val, l)
    DFS(root.right, val, l)
    
def branchSums(root):
    l = []
    DFS(root, 0, l)
    return l


def main():
    tree = { "nodes": [
    {"id": "1", "left": "2", "right": "3", "value": 1},
    {"id": "2", "left": "4", "right": "5", "value": 2},
    {"id": "3", "left": "6", "right": "7", "value": 3},
    {"id": "4", "left": "8", "right": "9", "value": 4},
    {"id": "5", "left": "10", "right": None, "value": 5},
    {"id": "6", "left": None, "right": None, "value": 6},
    {"id": "7", "left": None, "right": None, "value": 7},
    {"id": "8", "left": None, "right": None, "value": 8},
    {"id": "9", "left": None, "right": None, "value": 9},
    {"id": "10", "left": None, "right": None, "value": 10}
    ],
    "root": "1"
    }
    print(tree)

main()

