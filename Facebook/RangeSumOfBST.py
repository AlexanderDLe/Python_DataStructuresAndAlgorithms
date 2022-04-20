'''

  938. Range Sum of BST

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

def rangeSumBST(root, low, high):
  sum = 0

  def DFS(n):
    nonlocal sum, low, high
    if n is None: return

    if n.val >= low and n.val <= high: sum += n.val
    DFS(n.left)
    DFS(n.right)

  DFS(root)
  return sum



def buildTree():
  t = TreeNode(10)
  t.L = TreeNode(5)
  t.R = TreeNode(15)
  t.L.L = TreeNode(3)
  t.L.R = TreeNode(7)
  t.R.R = TreeNode(18)
  return t

t = buildTree()
print(rangeSumBST(t, 7, 15))