'''

  987. Vertical Order Traversal of a Binary Tree

  {
    -1: {
      0: [...],
      1: [...]
    },
    0: {
      0: [...],
      1: [...]
    }
  }

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode



def verticalTraversal(root):
  if root is None: return []

  colToRow = {}
  queue = [(root, 0, 0)]
  count = 1
  
  while queue:
    while count > 0:
      node, row, col = queue.pop(0)

      if col not in colToRow: colToRow[col] = {}
      if row not in colToRow[col]: colToRow[col][row] = []
      colToRow[col][row].append(node.val)

      if node.left : queue.append((node.left,  row + 1, col - 1))
      if node.right: queue.append((node.right, row + 1, col + 1))

      count -= 1

    count = len(queue)

  result = []
  sortedByCols = sorted(colToRow.items(), key = lambda x: x[0])
  for item in sortedByCols:
    # rows = {1:[], 2:[]...}
    rows = item[1]

    # sortedRows = [(1, [...]), (2, [...])]
    sortedRows = sorted(rows.items(), key = lambda x: x[0])

    res = []
    for row in sortedRows:
      row[1].sort()
      res += row[1]

    result.append(res)
      

  return result


def buildTree():
  t = TreeNode(3)
  t.left = TreeNode(9)
  t.right = TreeNode(20)
  t.right.left = TreeNode(15)
  t.right.right = TreeNode(7)
  return t
t = buildTree()
print(verticalTraversal(t))