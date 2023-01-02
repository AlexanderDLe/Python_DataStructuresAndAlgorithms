'''

  1642. Furthest Building You Can Reach
  
'''

from heapq import heappush, heappop

class SolutionSlowDP:
  def furthestBuilding(self, heights, bricks, ladders):
    n = len(heights)
    DP = {}
    
    def DFS(index, bricksLeft, laddersLeft):
      if (index, bricksLeft, laddersLeft) in DP: return DP[index, bricksLeft, laddersLeft]
      if index == n - 1: return n - 1
      
      currHeight = heights[index]
      nextHeight = heights[index + 1]
      maxDistance = index
      
      if currHeight >= nextHeight:
        maxDistance = max(maxDistance, DFS(index + 1, bricksLeft, laddersLeft))
      
      if currHeight < nextHeight and laddersLeft > 0:
        maxDistance = max(maxDistance, DFS(index + 1, bricksLeft, laddersLeft - 1))
        
      if currHeight < nextHeight and bricksLeft >= nextHeight - currHeight:
        diff = nextHeight - currHeight
        maxDistance = max(maxDistance, DFS(index + 1, bricksLeft - diff, laddersLeft))
      
      DP[index, bricksLeft, laddersLeft] = maxDistance
      return maxDistance        
    
    return DFS(0, bricks, ladders)
  
class MaxHeapNode:
  def __init__(self, val):
    self.val = val
  def __lt__(self, other):
    return self.val > other.val
  
class Solution:
  def furthestBuilding(self, heights, bricks, ladders):
    n = len(heights)
    maxHeap = []
    
    for i in range(n - 1):
      currHeight = heights[i]
      nextHeight = heights[i + 1]
      if currHeight >= nextHeight: continue
      
      diff = nextHeight - currHeight
      bricks -= diff
      heappush(maxHeap, MaxHeapNode(diff))
      
      # If we run out of bricks, then we swap a ladder for
      # the greatest brick height possible using maxHeap (brilliant)
      if bricks < 0:
        bricks += heappop(maxHeap).val
        
        if ladders > 0: ladders -= 1
        else: return i
        
    return n - 1
      

def runSolution():
  solution = Solution()
  print(solution.furthestBuilding(
    heights = [4,2,7,6,9,14,12], bricks = 5, ladders = 1))
  print(solution.furthestBuilding(
    heights = [4,12,2,7,3,18,20,3,19], bricks = 10, ladders = 2))
  print(solution.furthestBuilding(
    heights = [14,3,19,3], bricks = 17, ladders = 0))
  pass
runSolution()