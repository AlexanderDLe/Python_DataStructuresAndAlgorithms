'''

  1650. Lowest Common Ancestor of a Binary Tree III

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

def getDepth(n):
  count = 0

  while n != None:
    count += 1
    n = n.parent

  return count


def lowestCommonAncestor(p, q):
  pDepth = getDepth(p)
  qDepth = getDepth(q)

  while pDepth != qDepth:
    if pDepth < qDepth:
      qDepth -= 1
      q = q.parent

    if pDepth > qDepth:
      pDepth -= 1
      p = p.parent

  while p != q:
    p = p.parent
    q = q.parent

  return p

def buildTree():
  t = TreeNode(3)

  t.L = TreeNode(5)
  t.L.parent = t

  t.R = TreeNode(1)
  t.R.parent = t

  t.L.L = TreeNode(6)
  t.L.R = TreeNode(2)
  t.L.L.parent = t.L
  t.L.R.parent = t.L

  t.R.L = TreeNode(0)
  t.R.R = TreeNode(8)
  t.R.L.parent = t.R
  t.R.R.parent = t.R

  t.L.R.L = TreeNode(7)
  t.L.R.R = TreeNode(4)
  t.L.R.L.parent = t.L.R
  t.L.R.R.parent = t.L.R

  return (t.L, t.R)

p, q = buildTree()
print(lowestCommonAncestor(p, q))