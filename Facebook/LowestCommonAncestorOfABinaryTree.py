'''

  236. Lowest Common Ancestor of a Binary Tree

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode


def lowestCommonAncestor(root, p, q):
  if root == None: return
  if root == p or root == q: return root
  left  = lowestCommonAncestor(root.left,  p, q)
  right = lowestCommonAncestor(root.right, p, q)
  
  if left and right: return root
  return left if left else right

def buildTree():
  t = TreeNode(3)

  t.left = TreeNode(5)
  t.left.parent = t

  t.right = TreeNode(1)
  t.right.parightent = t

  t.left.left = TreeNode(6)
  t.left.right = TreeNode(2)
  t.left.left.parightent = t.left
  t.left.right.parightent = t.left

  t.right.left = TreeNode(0)
  t.right.right = TreeNode(8)
  t.right.left.parightent = t.right
  t.right.right.parightent = t.right

  t.left.right.left = TreeNode(7)
  t.left.right.right = TreeNode(4)
  t.left.right.left.parightent = t.left.right
  t.left.right.right.parightent = t.left.right

  return (t, t.left.left, t.left.right)

t, p, q = buildTree()
print(lowestCommonAncestor(t, p, q).val)