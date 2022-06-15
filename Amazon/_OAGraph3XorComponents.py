'''

  A tree is defined by edges.
  
  Divide this tree into three connected components by cutting any
  two edges of the tree.
  
  Divide the connected components in such a way that the maximum and minimum
  XOR values of all the vertices in each connection is minimized.
  
  Example:
  
  edges = [[1,2], [2,3], [4,1]]
  
          1                1
        /   \            /
       2     4    ->    2     4
      /   
     3                3
  
  Removed edges [2,3] and [1,4]
                                      XOR of all values:
  Component 1 = [1,2]                 1^2 = 3
  Component 2 = [3]                   3 = 3
  Component 3 = [4]                   4 = 4
  
  Max = 4
  Min = 3
  result = 4 - 3 = 1
  
  ----------------------------------------------
  
  If N = 5, Edges = [[1, 2], [1, 4], [1, 5], [3, 4]]

  You can cut the edge between 3 and 4 and the edge between 1 and 4.
  
  The Components are now C1={1, 2, 5}, C2={3} and C3={4}. 
  So, the XOR values are X1=6(1 XOR 2 XOR 5), X2=3 and X3=4.
  
  Thus the answer is 6 - 3 = 3.
'''

from collections import defaultdict
import functools
import math
from math import inf
import operator

class DisjointSetRef:
  def __init__(self, n):
    self.parent = {i:i for i in range(1, n + 1)}

  def find(self, node):
    if node != self.parent[node]:
      self.parent[node] = self.find(self.parent[node])
    return self.parent[node]

  def union(self, x, y):
    x = self.find(x)
    y = self.find(y)
    self.parent[x] = y
  
  def groups(self):
    table = defaultdict(lambda: set())
    for node in self.parent:
      group = table[self.find(node)]
      group.add(node)
    return list(map(list, table.values()))
class SolutionRef:
  def func(self, n, edges):
    result = math.inf
    
    for i in range(len(edges)):
      for j in range(i + 1, len(edges)):
        disjoint = DisjointSet(n)
        
        for k, (u, v) in enumerate(edges):
          if k != i and k != j:
            disjoint.union(u, v)
        
        c1, c2, c3 = disjoint.groups()        
        x1 = self.calcXOR(c1)
        x2 = self.calcXOR(c2)
        x3 = self.calcXOR(c3)
        result = min(result, max(x1, x2, x3) - min(x1, x2, x3))
    return result
  
  def calcXOR(self, group):
    curr = group[0]
    for i in range(1, len(group)):
      curr ^= group[i]
    return curr
      
class DisjointSet:
  def __init__(self, parents):
    self.parents = parents
    
  def find(self, node):
    if node != self.parents[node]:
      self.parents[node] = self.find(self.parents[node])
    return self.parents[node]
  
  def union(self, x, y):
    xRoot, yRoot = self.find(x), self.find(y)
    self.parents[xRoot] = yRoot
    
  def getGroups(self):
    groups = defaultdict(lambda: set())
    for node in self.parents:
      group = groups[self.find(node)]
      group.add(node)
    # print(list(groups.values()))
    return list(map(list, groups.values()))
      

class Solution:
  def func(self, n, edges):
    result = inf
    parents = {i:i for i in range(1, n + 1)}
    
    for i in range(len(edges)):
      for j in range(i + 1, len(edges)):
        disjoint = DisjointSet(parents.copy())
        
        for k, (u, v) in enumerate(edges):
          if k == i or k == j: continue
          disjoint.union(u, v)
        
        c1, c2, c3 = disjoint.getGroups()
        x1 = self.calcXOR(c1)
        x2 = self.calcXOR(c2)
        x3 = self.calcXOR(c3)
        result = min(result, max(x1, x2, x3) - min(x1, x2, x3))
    
    return result
  
  def calcXOR(self, group):
    curr = group[0]
    for i in range(1, len(group)):
      curr ^= group[i]
    return curr
  
def runSolution():
  solution = Solution()
  print(solution.func(4, [[1,2], [2,3], [4,1]]))
  print(solution.func(5, [(1, 2), (1, 4), (1, 5), (3, 4)]))
  pass
runSolution()