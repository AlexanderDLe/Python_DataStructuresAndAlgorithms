'''

  156. Binary Tree Upside Down

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode


class SolutionRef:
  def upsideDownBinaryTree(self, root):
    if not root or not root.left: return root
    
    res = self.upsideDownBinaryTree(root.left)
    
    root.left.right = root
    if root.right: root.left.left = root.right
    
    root.left = None
    root.right = None
    return res

class Solution:
  def upsideDownBinaryTree(self, root):
    if root == None or root.left == None: return root
    
    res = self.upsideDownBinaryTree(root.left)
    
    root.left.right = root
    if root.right: root.left.left = root.right
    
    root.left = None
    root.right = None    
    return res
  
  
  
def runSolution():
  t = TreeNode(1)
  t.left = TreeNode(2)
  t.right = TreeNode(3)
  t.left.left = TreeNode(4)
  t.left.right = TreeNode(5)
  
  solution = Solution()
  print(solution.upsideDownBinaryTree())
  pass
runSolution()