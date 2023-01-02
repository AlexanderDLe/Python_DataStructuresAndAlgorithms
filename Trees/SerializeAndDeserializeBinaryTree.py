'''

  297. Serialize and Deserialize Binary Tree

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)

from DataStrucutres import TreeNode
from _utils import preorderTraversal

class CodecMess:
  def serialize(self, root):
    result = ''
    
    def DFS(n):
      nonlocal result
      
      if n == None:
        result += 'None,'
        return
      
      result += str(n.val) + ','
      DFS(n.left)
      DFS(n.right)
      
      return result
    
    DFS(root)
    return result

  def deserialize(self, data):
    arr = data.split(',')
    arr.pop()
    index = 0
    
    def build():
      nonlocal index
      
      if index == len(arr): return
      
      if arr[index] == 'None':
        index += 1
        return None
      
      num = int(arr[index])
      node = TreeNode(num)
      index += 1
      node.left = build()
      node.right = build()
      
      return node
  
    return build()
  
  
class Codec:
  def serialize(self, root):
    if not root: return 'x'
    return root.val, self.serialize(root.left), self.serialize(root.right)

  def deserialize(self, data):
    if data[0] == 'x': return None
    
    node = TreeNode(data[0])
    node.left = self.deserialize(data[1])
    node.right = self.deserialize(data[2])
    
    return node
  
  
  
  
  

def runSolution():
  t1 = TreeNode(1)
  t1.left = TreeNode(2)
  t1.right = TreeNode(3)
  t1.right.left = TreeNode(4)
  t1.right.right = TreeNode(5)
  
  t2 = TreeNode(1)
  t2.left = TreeNode(2)
  t2.right = TreeNode(2)
  t2.left.left = TreeNode(3)
  t2.left.right = TreeNode(3)
  t2.left.left.left = TreeNode(4)
  t2.left.left.right = TreeNode(4)
  
  solution = Codec()
  
  s1 = solution.serialize(t1)
  print(s1)
  
  s2 = solution.serialize(t2)
  print(s2)
  
  preorderTraversal(solution.deserialize(s1))
  preorderTraversal(solution.deserialize(s2))
  pass
runSolution()

