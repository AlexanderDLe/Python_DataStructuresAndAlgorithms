'''

  99. Recover Binary Search Tree

'''

import os, sys
from turtle import right
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class SolutionRef:
  def recoverTree(self, root):
    self.prev  = TreeNode(float('-inf'))
    self.nodeA = None
    self.nodeB = None
    
    self.traverse(root)
    self.nodeA.val, self.nodeB.val = self.nodeB.val, self.nodeA.val
    
  def traverse(self, n):
    if not n: return
    
    self.traverse(n.left)
    
    if self.nodeA == None and self.prev.val >= n.val: self.nodeA = self.prev
    if self.nodeA != None and self.prev.val >= n.val: self.nodeB = n
    self.prev = n
    
    self.traverse(n.right)
    
  

class Solution:
  def recoverTree(self, root):
    self.prev  = TreeNode(float('-inf'))
    self.nodeA = None
    self.nodeB = None
    
    self.traverse(root)
  
  def traverse(self, n):
    if not n: return
    
    self.traverse(n.left)
    
    if self.nodeA == None and self.prev.val >= n.val: self.nodeA = self.prev
    if self.nodeA != None and self.prev.val >= n.val: self.nodeB = n
    self.prev = n
    
    self.traverse(n.right)
  

def runSolution():
  t1 = TreeNode(1)
  t1.left = TreeNode(3)
  t1.left.right = TreeNode(2)
  
  t2 = TreeNode(3)
  t2.left = TreeNode(1)
  t2.right = TreeNode(4)
  t2.right.left = TreeNode(2)
  
  solution = Solution()
  print(solution.recoverTree(t1))
  print(solution.recoverTree(t2))
  pass
runSolution()

