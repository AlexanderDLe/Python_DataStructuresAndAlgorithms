'''

  2. Add Two Numbers

'''

from collections import Counter
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode

class Solution:
  def findDuplicateSubtrees(self, root):
    result = []
    pathFreq = Counter()
    
    def DFS(n):
      if not n: return '#'
      
      path = str(n.val) + '-' + DFS(n.left) + DFS(n.right)
      
      pathFreq[path] += 1      
      if pathFreq[path] == 2:
        result.append(n)
      
      return path
    
    DFS(root)
    return result
  

def runSolution():
  t1 = TreeNode(1)
  t1.left = TreeNode(2)
  t1.right = TreeNode(3)
  t1.left.left = TreeNode(4)
  t1.right.left = TreeNode(2)
  t1.right.right = TreeNode(4)
  t1.right.left.left = TreeNode(4)
  
  t2 = TreeNode(2)
  t2.left = TreeNode(1)
  t2.right = TreeNode(1)
  
  t3 = TreeNode(2)
  t3.left = TreeNode(2)
  t3.right = TreeNode(2)
  t3.left.left = TreeNode(3)
  t3.right.left = TreeNode(3)
  
  t4 = TreeNode(2)
  t4.left = TreeNode(1)
  t4.right = TreeNode(11)
  t4.left.left = TreeNode(11)
  t4.right.left = TreeNode(1)
  
  solution = Solution()
  print(solution.findDuplicateSubtrees(t1))
  print(solution.findDuplicateSubtrees(t2))
  print(solution.findDuplicateSubtrees(t3))
  print(solution.findDuplicateSubtrees(t4))
  pass
runSolution()

