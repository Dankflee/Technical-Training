class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preorderTraversal(root):
  if root is None:
    return
  print(root.data, end=" ")
  preorderTraversal(root.left)
  preorderTraversal(root.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.right = Node(5)

print("Preorder traverse of tree is : ", end="")
preorderTraversal(root)