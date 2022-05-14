'''

  1448. Count Good Nodes in Binary Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

class Solution:
  def goodNodes(self, root):
    count = 0
    
    def DFS(n, maxVal):
      nonlocal count
      if not n: return
      if n.val >= maxVal: count += 1
      
      DFS(n.left, max(maxVal, n.val))
      DFS(n.right, max(maxVal, n.val))
    
    DFS(root, float('-inf'))
    return count

def runSolution():
  t1 = TreeNode(3)
  t1.left = TreeNode(1)
  t1.right = TreeNode(4)
  t1.left.left = TreeNode(3)
  t1.right.left = TreeNode(1)
  t1.right.right = TreeNode(5)
  
  t2 = TreeNode(3)
  t2.left = TreeNode(3)
  t2.left.left = TreeNode(4)
  t2.left.right = TreeNode(2)
  
  solution = Solution()
  print(solution.goodNodes(t1))
  print(solution.goodNodes(t2))
  pass
runSolution()

