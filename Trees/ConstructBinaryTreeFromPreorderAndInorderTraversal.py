'''

  105. Construct Binary Tree from Preorder and Inorder Traversal

'''

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode



class Solution:
  def buildTree(self, preorder, inorder):
    preToInorderIndex = {preVal: inorder.index(preVal) for preVal in preorder}
    preIndex = 0
    
    def build(inStart, inEnd):
      nonlocal preIndex
      if preIndex >= len(preorder) or inStart > inEnd: return None
      
      preVal = preorder[preIndex]
      preIndex += 1
      
      node = TreeNode(preVal)
      inIndex = preToInorderIndex[preVal]
      
      
      node.left = build(inStart, inIndex - 1)
      node.right = build(inIndex + 1, inEnd)
      return node
      
    return build(0, len(preorder))
    
    

def runSolution():
  solution = Solution()
  print(solution.buildTree(preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]))
  print(solution.buildTree(preorder = [-1], inorder = [-1]))
  pass
runSolution()

