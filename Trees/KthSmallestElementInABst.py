'''

  98. Validate Binary Search Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

class Solution:
  def kthSmallest(self, root, k):
    value = -1
    
    def DFS(n):
      nonlocal value, k
      if not n or k <= 0: return
      
      DFS(n.left)
      k -= 1
      if k == 0: value = n.val
      DFS(n.right)
    
    DFS(root)
    return value

def runSolution():
  t1 = TreeNode(3)
  t1.left = TreeNode(1)
  t1.right = TreeNode(4)
  t1.left.right = TreeNode(2)

  t2 = TreeNode(5)
  t2.left = TreeNode(3)
  t2.right = TreeNode(6)
  t2.left.left = TreeNode(2)
  t2.left.right = TreeNode(4)
  t2.left.left.left = TreeNode(1)
  
  solution = Solution()
  print(solution.kthSmallest(t1, 1))
  print(solution.kthSmallest(t2, 3))
  pass
runSolution()

