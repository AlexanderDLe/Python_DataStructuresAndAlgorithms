'''

  543. Diameter of Binary Tree

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

def diameterofBinaryTree(root):
  maxDiameter = 0

  def DFS(n):
    if n == None: return 0
    nonlocal maxDiameter

    left = DFS(n.left)
    right = DFS(n.right)
    maxDiameter = max(maxDiameter, left + right)

    return 1 + max(left, right)


  DFS(root)
  return maxDiameter



def buildTree():
  t = TreeNode(1)
  t.left = TreeNode(2)
  t.right = TreeNode(3)
  t.left.left = TreeNode(4)
  t.left.right = TreeNode(5)
  return t
t = buildTree()
print(diameterofBinaryTree(t))