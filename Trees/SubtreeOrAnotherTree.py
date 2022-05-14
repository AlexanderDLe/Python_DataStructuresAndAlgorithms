'''

  572. Subtree of Another Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode

class Solution:
  def isSubtree(self, root, subRoot):
    match = False
    
    def DFS(n):
      nonlocal match
      if not n or match == True: return
      if n.val == subRoot.val and self.checkMatch(n, subRoot):
        match = True
        
      DFS(n.left)
      DFS(n.right)
    
    DFS(root)
    return match
  
  def checkMatch(self, p, q):
    if p and q and p.val != q.val: return False
    if p and not q: return False
    if q and not p: return False
    if not p and not q: return True
    
    return self.checkMatch(p.left, q.left) and self.checkMatch(p.right, q.right)

def runSolution():
  t1 = TreeNode(3)
  t1.left = TreeNode(4)
  t1.right = TreeNode(5)
  t1.left.left = TreeNode(1)
  t1.left.right = TreeNode(2)

  t2 = TreeNode(3)
  t2.left = TreeNode(4)
  t2.right = TreeNode(5)
  t2.left.left = TreeNode(1)
  t2.left.right = TreeNode(2)
  t2.left.right.left = TreeNode(0)
  
  t3 = TreeNode(4)
  t3.left = TreeNode(1)
  t3.right = TreeNode(2)
  
  
  solution = Solution()
  print(solution.isSubtree(t1, t3))
  print(solution.isSubtree(t2, t3))
  pass
runSolution()

