'''

  515. Find Largest Value in Each Tree Row

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode as TN


def largestValues(root):
  if root == None: return []

  result = []
  queue = [root]
  count = 1

  while queue:
    levelMax = float('-inf')

    while count:
      node = queue.pop(0)
      levelMax = max(levelMax, node.val)

      if node.left : queue.append(node.left)
      if node.right: queue.append(node.right)

      count -= 1
    result.append(levelMax)
    count = len(queue)

  return result


def buildTree():
  t = TN(1)
  t.left = TN(3)
  t.right = TN(2)
  t.left.left = TN(5)
  t.left.right = TN(3)
  t.right.right = TN(9)
  return t

print(largestValues(buildTree()))