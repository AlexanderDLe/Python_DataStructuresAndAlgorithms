'''

  272. Closest Binary Search Tree Value 2

'''
import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from DataStrucutres import TreeNode as node
import heapq


class Node:
  def __init__(self, value, distance):
    self.value = value
    self.distance = distance
  def __repr__(self):
    return f'Node:{self.value}|{self.distance}'
  def __lt__(self, other):
    return self.distance > other.distance

class Solution:
  def closestKValues(self, root, target, k):
    heap = []
    
    def DFS(n):
      if n == None: return
      distance = abs(target - n.val)
      
      if len(heap) < k:
        heapq.heappush(heap, Node(n.val, distance))
      elif distance < heap[0].distance:
        heapq.heappop(heap)
        heapq.heappush(heap, Node(n.val, distance))
        
      DFS(n.left)
      DFS(n.right)
      
      
    DFS(root)
    return list(map(lambda x: x.value, heap))
  
def runSolution():
  t = node(4)
  t.left = node(2)
  t.right = node(5)
  t.left.left = node(1)
  t.left.right = node(3)
  
  solution = Solution()
  print(solution.closestKValues(root = t, target = 3.714286, k = 2))
  pass
runSolution()