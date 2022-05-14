'''

  2. Add Two Numbers

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution:
  def isBalanced(self, root):
    if not root: return True
    
    balanced = True
    
    def DFS(n):
      nonlocal balanced
      if not n: return 0
      
      left = DFS(n.left)
      right = DFS(n.right)
      
      if not balanced: return
      if abs(left - right) > 1: balanced = False
      
      return 1 + max(left, right)
    
    DFS(root)
    return balanced
  

def runSolution():
  t1 = TreeNode(3)
  t1.left = TreeNode(9)
  t1.right = TreeNode(20)
  t1.right.left = TreeNode(15)
  t1.right.right = TreeNode(7)
  
  t2 = TreeNode(1)
  t2.left = TreeNode(2)
  t2.right = TreeNode(2)
  t2.left.left = TreeNode(3)
  t2.left.right = TreeNode(3)
  t2.left.left.left = TreeNode(4)
  t2.left.left.right = TreeNode(4)
  
  solution = Solution()
  print(solution.isBalanced(t1))
  print(solution.isBalanced(t2))
  pass
runSolution()

