'''

  235. Lowest Common Ancestor of a Binary Search Tree

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution1:
  def lowestCommonAncestor(self, root, p, q):
    if not root or root == p or root == q: return root
    
    left = self.lowestCommonAncestor(root.left, p, q)
    right = self.lowestCommonAncestor(root.right, p, q)
    
    if left and right: return root
    return left if left else right

class Solution:
  def lowestCommonAncestor(self, root, p, q):
    if p.val < root.val and q.val < root.val:
      return self.lowestCommonAncestor(root.left, p, q)
      
    elif p.val > root.val and q.val > root.val:
      return self.lowestCommonAncestor(root.right, p, q)
      
    return root
      
  

def runSolution():
  t = TreeNode(6)
  t.left = TreeNode(2)
  t.right = TreeNode(8)
  t.left.left = TreeNode(0)
  t.left.right = TreeNode(4)
  t.left.right.left = TreeNode(3)
  t.left.right.right = TreeNode(5)
  t.right.left = TreeNode(7)
  t.right.right = TreeNode(9)
  
  solution = Solution()
  print(solution.lowestCommonAncestor(t, t.left, t.right))
  print(solution.lowestCommonAncestor(t, t.left.left, t.left.right.left))
  pass
runSolution()

