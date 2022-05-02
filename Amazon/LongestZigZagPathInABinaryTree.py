'''

  1372. Longest ZigZag Path in a Binary Tree


          1
         / \  
        2   3
            /\
           6  7
          / \
         8   9 
'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode as node

class SolutionRef:
  def longestZigZag(self, root):    
    def DFS(n):
      if n == None: return 0, 0
      
      _, leftR  = DFS(n.left)
      rightL, _ = DFS(n.right)
      
      self.longest = max(self.longest, leftR + 1, rightL + 1)
      return leftR + 1, rightL + 1
      
    self.longest = 0
    DFS(root)
    return self.longest - 1  
  
class Solution:
  def longestZigZag(self, root):    
    
    def DFS(n):
      if n == None: return (0, 0)      
      _, leftR  = DFS(n.left)
      rightL, _ = DFS(n.right)
      self.longest = max(self.longest, leftR + 1, rightL + 1)      
      return (leftR + 1, rightL + 1)      
    
    self.longest = 0
    DFS(root)
    return self.longest - 1
  
def runSolution():
  t = node(1)
  t.right = node(1)
  t.right.right = node(1)
  t.right.left = node(1)
  t.right.right.right = node(1)
  t.right.right.left = node(1)
  t.right.right.left.right = node(1)
  t.right.right.left.right.right = node(1)
  
  solution = Solution()
  print(solution.longestZigZag(t))
  pass
runSolution()