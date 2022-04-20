'''

  129. Sum Root to Leaf Numbers

'''

import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode as Node

def sumNumbers(root):
  sum = 0

  def DFS(n, num):
    nonlocal sum
    if n == None: return
    if n.left == None and n.right == None:
      sum += int(num + str(n.val))
      return
    
    DFS(n.left, num + str(n.val))
    DFS(n.right, num + str(n.val))

  DFS(root, '0')
  return sum



def buildTree():
  t = Node(4)
  t.left = Node(9)
  t.right = Node(0)
  t.left.left = Node(5)
  t.left.right = Node(1)
  return t
print(sumNumbers(buildTree()))
