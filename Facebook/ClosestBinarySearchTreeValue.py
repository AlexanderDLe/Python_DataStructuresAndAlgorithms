'''

  270. Closest Binary Search Tree Value

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode as TN

def closestValue(root, target):
  closest = 0
  minDistance = float('inf')
  
  def DFS(n):
    nonlocal minDistance, closest
    if n == None: return
    distance = abs(target - n.val)
    if distance < minDistance:
      minDistance = distance
      closest = n.val
    
    DFS(n.left)
    DFS(n.right)

  DFS(root)
  return closest


def buildTree():
  t = TN(4)
  t.left = TN(2)
  t.right = TN(5)
  t.left.left = TN(1)
  t.left.right = TN(3)
  return t
print(closestValue(buildTree(), 3.7))