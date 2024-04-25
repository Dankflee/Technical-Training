class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def preOrderTraversal(root):
  if root is None:
    return

  # 1. Visit the root node
  print(root.data, end=" ")

  # 2. Recursively traverse the left subtree
  preOrderTraversal(root.left)

  # 3. Recursively traverse the right subtree
  preOrderTraversal(root.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(6)
root.left.left.left = Node(8)
root.left.left.right = Node(9)
root.right.right = Node(5)

print("Preorder traverse of tree is : ", end="")
preOrderTraversal(root)