'''

  199. Binary Tree Right Side View

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

def rightSideView(root):
  if root == None: return []

  queue = [root]
  count = 1
  result = []
  
  while queue:
    while count:
      node = queue.pop(0)
      if count == 1: result.append(node.val)

      if node.left : queue.append(node.left)
      if node.right: queue.append(node.right)

      count -= 1

    count = len(queue)

  return result


def buildTree():
  t = TreeNode(1)
  t.left = TreeNode(2)
  t.right = TreeNode(3)
  t.left.right = TreeNode(5)
  t.right.right = TreeNode(4)
  return t

t = buildTree()
print(rightSideView(t))