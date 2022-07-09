'''

  AlgoExpert A Star

'''

from heapq import heappop, heappush


class Solution:
  def AStar(self, startRow, startCol, endRow, endCol, graph):
    self.rows, self.cols = len(graph), len(graph[0])
    self.endRow, self.endCol, self.graph = endRow, endCol, graph
    
    hScore = self.getManhattanDistance(startRow, startCol)
    minHeap = [(hScore, 0, startRow, startCol)] # (score, distance, row, col)
    self.visited = set([(startRow, startCol)])
    
    while minHeap:
      _, distance, row, col  = heappop(minHeap)
      
      if row == endRow and col == endCol: return distance
      
      for xDir, yDir in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        nextRow, nextCol = row + xDir, col + yDir
        
        if self.invalid(nextRow, nextCol): continue
        
        self.visited.add((nextRow, nextCol))
        nextHScore = self.getManhattanDistance(nextRow, nextCol)
        nextDistance = distance + 1
        heappush(minHeap, (nextDistance + nextHScore, nextDistance, nextRow, nextCol))
      
    return -1
    
  def getManhattanDistance(self, row, col):
    return abs(row - self.endRow) + abs(col - self.endCol)

  def invalid(self, row, col):
    if row < 0 or row == self.rows: return True
    if col < 0 or col == self.cols: return True
    if self.graph[row][col] == 1  : return True
    if (row, col) in self.visited : return True
    return False
    
    
  
def runSolution():
  solution = Solution()
  print(solution.AStar(
    startRow = 0,
    startCol = 1,
    endRow = 4,
    endCol = 3,
    graph = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [1, 0, 1, 1, 1],
    [0, 0, 0, 0, 0],
  ]))
  pass
runSolution()