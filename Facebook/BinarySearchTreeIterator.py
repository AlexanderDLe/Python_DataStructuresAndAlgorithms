'''

  173. Binary Search Tree Iterator

'''
import os, sys
from tkinter.messagebox import NO
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class BSTIterator:
  def __init__(self, root):
    self.stack = []

    while root and root.left:
      self.stack.append(root)
      root = root.left

    self.curr = root

  def next(self) -> int:
    val = self.curr.val
    curr = self.curr

    # Try going right before going back up
    if curr.right:
      curr = curr.right
      while curr.left:
        self.stack.append(curr)
        curr = curr.left
        
    # If there is no right node, go up one level
    else:
      curr = self.stack.pop() if self.stack else None

    self.curr = curr
    return val

  def hasNext(self) -> bool:
    return self.curr != None




def buildTree():
  t = TreeNode(7)
  t.left = TreeNode(3)
  t.right = TreeNode(15)
  t.right.left = TreeNode(9)
  t.right.right = TreeNode(20)
  return t

obj = BSTIterator(buildTree())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.next())
print(obj.hasNext())