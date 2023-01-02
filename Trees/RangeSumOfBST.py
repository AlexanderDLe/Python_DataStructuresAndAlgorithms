'''

  938. Range Sum of BST

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode


class SolutionRef:
  def rangeSumBST(self, root, low, high):
    sum = 0

    def DFS(n):
      nonlocal sum, low, high
      if n is None: return

      if n.val >= low and n.val <= high: sum += n.val
      DFS(n.left)
      DFS(n.right)

    DFS(root)
    return sum

class Solution:
  
  '''
  
    Time Complexity
    O(n) DFS through all nodes
    
    Space Complexity
    O(h) the call stack will be at most the height of the tree in memory
  
  '''
  
  def rangeSumBST(self, root, low, high):
    if root == None: return 0
    
    left  = self.rangeSumBST(root.left, low, high)
    right = self.rangeSumBST(root.right, low, high)
    value = root.val if low <= root.val <= high else 0
    
    return value + left + right
    
  
def runSolution():
  t = TreeNode(10)
  t.left = TreeNode(5)
  t.right = TreeNode(15)
  t.left.left = TreeNode(3)
  t.left.right = TreeNode(7)
  t.right.right = TreeNode(18)

  solution = Solution()
  print(solution.rangeSumBST(t, 7, 15))
  pass
runSolution()
