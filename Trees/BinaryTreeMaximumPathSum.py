'''

  124. Binary Tree Maximum Path Sum

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution:
  def maxPathSum(self, root):
    maxPath = root.val
    
    def DFS(n):
      if not n: return 0
      
      left = DFS(n.left)
      right = DFS(n.right)
      curr = n.val
      
      nonlocal maxPath
      maxPath = max(maxPath, curr, left + right + curr, curr + max(left, right))
      return max(curr, curr + max(left, right))
    
    DFS(root)
    return maxPath
  

def runSolution():
  t1 = TreeNode(1)
  t1.left = TreeNode(2)
  t1.right = TreeNode(3)
  
  t2 = TreeNode(-10)
  t2.left = TreeNode(9)
  t2.right = TreeNode(20)
  t2.right.left = TreeNode(15)
  t2.right.right = TreeNode(7)
  
  solution = Solution()
  print(solution.maxPathSum(t1))
  print(solution.maxPathSum(t2))
  pass
runSolution()

