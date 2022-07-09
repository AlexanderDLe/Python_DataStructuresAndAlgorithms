'''

  1632. Rank Transform of a Matrix

'''

from collections import defaultdict
from itertools import product


class UnionFind:
  def __init__(self, graph):
    self.roots = {i:i for i in graph}
  
  def find(self, x):
    roots = self.roots
    if roots[x] != x:
      roots[x] = self.find(roots[x])
    return roots[x]
  
  def union(self, x, y):
    xRoot, yRoot = self.find(x), self.find(y)
    self.roots[xRoot] = yRoot
    
  def groups(self):
    ans = defaultdict(list)
    for key in self.roots.keys():
      ans[self.find(key)].append(key)
    return ans

class SolutionRef:
  def matrixRankTransform(self, matrix):
    rows, cols = len(matrix), len(matrix[0])
    rank = [0] * (rows + cols)
    map = defaultdict(list)
    
    for row, col in product(range(rows), range(cols)):
      map[matrix[row][col]].append((row, col))
    
    for val in sorted(map):
      coords = map[val]
      graph = [row for row, _ in coords] + [col + rows for _, col in coords]
      UF = UnionFind(graph)
      
      for row, col in coords: UF.union(row, col + rows)
      
      for group in UF.groups().values():
        maxRank = max(rank[i] for i in group)
        for i in group: rank[i] = maxRank + 1
      
      for row, col in coords: matrix[row][col] = rank[i]
    
    return matrix
    
class Solution:
  def matrixRankTransform(self, matrix):
    rows, cols = len(matrix), len(matrix[0])
    ranks = [0] * (rows + cols)
    map = defaultdict(list)
    
    for row, col in product(range(rows), range(cols)):
      val = matrix[row][col]
      map[val].append((row, col))
      
    for val in sorted(list(map.keys())):
      coords = map[val]
      graph =  [row for row, _ in coords]
      graph += [col + rows for _, col in coords]
      
      UF = UnionFind(graph)
      
      for row, col in coords: UF.union(row, col + rows)
      
      for group in UF.groups().values():
        maxRank = max(ranks[i] for i in group)
        for i in group: ranks[i] = maxRank + 1
      
      for row, col in coords: matrix[row][col] = ranks[row]
        
    return matrix
  
def runSolution():
  solution = Solution()
  # print(solution.matrixRankTransform(matrix = [[1,2],[3,4]]))
  # print(solution.matrixRankTransform(matrix = [[7,7],[7,7]]))
  print(solution.matrixRankTransform(matrix = [[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]]))
  pass
runSolution()