'''

  98. Validate Binary Search Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

class Solution:
  def isValidBST(self, root):
    isValid = True
    
    def DFS(n, min, max):
      nonlocal isValid
      
      if not n or not isValid: return
      if n.val <= min or n.val >= max:
        isValid = False
        return

      DFS(n.left, min, n.val)
      DFS(n.right, n.val, max)
    
    DFS(root, float('-inf'), float('inf'))
    return isValid

def runSolution():
  t1 = TreeNode(2)
  t1.left = TreeNode(1)
  t1.right = TreeNode(3)

  t2 = TreeNode(5)
  t2.left = TreeNode(1)
  t2.right = TreeNode(4)
  t2.right.left = TreeNode(3)
  t2.right.right = TreeNode(6)
  
  
  solution = Solution()
  print(solution.isValidBST(t1))
  print(solution.isValidBST(t2))
  pass
runSolution()

