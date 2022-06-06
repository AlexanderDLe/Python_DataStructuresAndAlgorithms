'''

  1932. Merge BSTs to Create Single BST

'''

import os, sys
from turtle import right
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution:
  def recoverTree(self, root):
    pass
    
  

def runSolution():
  t0 = TreeNode(2)
  t0.left = TreeNode(1)
  
  t1 = TreeNode(3)
  t1.left = TreeNode(2)
  t1.right = TreeNode(5)
  
  t2 = TreeNode(5)
  t2.left = TreeNode(4)
  
  
  solution = Solution()
  print(solution.recoverTree([t0, t1, t2]))
  pass
runSolution()

