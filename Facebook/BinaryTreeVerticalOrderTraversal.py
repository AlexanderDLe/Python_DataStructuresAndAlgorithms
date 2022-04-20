'''

  314. Binary Tree Vertical Order Traversal

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)


from DataStrucutres import TreeNode


def verticalOrder(root):
  if root is None: return root
  
  colDict = {}
  queue = [(root, 0)]
  count = 1

  while queue:
    while count > 0:
      node, col = queue.pop(0)

      if col not in colDict: colDict[col] = []
      colDict[col].append(node.val)

      if node.left  is not None: queue.append((node.left, col - 1))
      if node.right is not None: queue.append((node.right, col + 1))
      count -= 1

    count = len(queue)
  
  sortedItems = sorted(colDict.items(), key=lambda x: x[0])
  return list(map(lambda x: x[1], sortedItems))





  

def buildTree():
  t1 = TreeNode(3)
  t1.left = TreeNode(9)
  t1.right = TreeNode(8)

  t1.left.left = TreeNode(4)
  t1.left.right = TreeNode(0)
  t1.right.left = TreeNode(1)
  t1.right.right = TreeNode(7)

  t1.left.right.right = TreeNode(2)
  t1.right.left.left = TreeNode(5)

  return t1
print(verticalOrder(buildTree()))