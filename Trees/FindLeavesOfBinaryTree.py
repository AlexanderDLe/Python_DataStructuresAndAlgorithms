'''

  366. Find Leaves of Binary Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode as Node

class Solution:
  def findLeaves(self, root):
    result = []
    
    while root.left or root.right:
      result.append(self.getLeaves(root))
    
    result.append([root.val])
    return result
  
  def getLeaves(self, root):
    leaves = []
    
    def DFS(n):
      if n == None: return False
      left  = DFS(n.left)
      right = DFS(n.right)      
      isLeaf = n.left == None and n.right == None
      
      if isLeaf: leaves.append(n.val)
      if left: n.left = None
      if right: n.right = None
      
      if isLeaf: return True
      else     : return False
    
    DFS(root)
    return leaves
  
  
def runSolution():
  t = Node(1)
  t.left = Node(2)
  t.right = Node(3)
  t.left.left = Node(4)
  t.left.right = Node(5)
  
  solution = Solution()
  print(solution.findLeaves(t))
  pass
runSolution()