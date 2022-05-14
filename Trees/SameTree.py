'''

  100. Same Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution:
  def isSameTree(self, p, q):
    if p and q and p.val != q.val: return False
    if p and not q: return False
    if q and not p: return False
    if not p and not q: return True
    
    return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
  

def runSolution():
  t1 = TreeNode(1)
  t1.left = TreeNode(2)
  t1.right = TreeNode(3)
  
  t2 = TreeNode(1)
  t2.left = TreeNode(2)
  t2.right = TreeNode(3)
  
  t3 = TreeNode(1)
  t3.left = TreeNode(2)
  
  solution = Solution()
  print(solution.isSameTree(t1, t2))
  print(solution.isSameTree(t1, t3))
  pass
runSolution()

