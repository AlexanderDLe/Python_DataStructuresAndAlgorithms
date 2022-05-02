'''

  545. Boundary of Binary Tree

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode as Node

class Solution:
  def boundaryOfBinaryTree(self, root):
    if not root: return []
    
    leftBoundary = self.getLeftBoundary(root)
    rightBoundary = self.getRightBoundary(root)
    leaves = self.getLeaves(root)
    
    result = []
    seen = set()
    
    self.buildResult(result, seen, leftBoundary)
    self.buildResult(result, seen, leaves)
    self.buildResult(result, seen, reversed(rightBoundary))
    
    return result

  def buildResult(self, result, seen, nodes):
    for node in nodes:
      if node in seen: continue
      seen.add(node)
      result.append(node.val)

  def getLeftBoundary(self, root):
    leftBoundary = [root]
    curr = root.left
    while curr:
      leftBoundary.append(curr)
      curr = curr.left or curr.right
    return leftBoundary
  
  def getRightBoundary(self, root):
    rightBoundary = [root]
    curr = root.right
    while curr:
      rightBoundary.append(curr)
      curr = curr.right or curr.left
    return rightBoundary
  
  def getLeaves(self, root):
    leaves = []
    
    def DFS(n):
      if not n: return
      if n.left == None and n.right == None: leaves.append(n)
      DFS(n.left)
      DFS(n.right)
      
    DFS(root)
    return leaves
  
def runSolution():
  solution = Solution()
  
  node = Node(1)
  node.left = Node(2)
  node.right = Node(3)
  node.left.left = Node(4)
  node.left.right = Node(5)
  node.left.right.left = Node(7)
  node.left.right.right = Node(8)
  node.right.left = Node(6)
  node.right.left.left = Node(9)
  node.right.left.right = Node(10)
  
  print(solution.boundaryOfBinaryTree(node))
  
runSolution()