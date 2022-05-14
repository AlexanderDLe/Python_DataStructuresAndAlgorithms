'''

  403. Frog Jump

'''

class SolutionRef:
  def canCross(self, stones):
    last = stones[-1]
    stoneSet = set(stones)
    stoneReached = set()
    
    def DFS(stone, k):
      if stone == last: return True
      if stone not in stoneSet: return False
      if (stone, k) in stoneReached: return False
      stoneReached.add((stone, k))
      
      if DFS(stone + k + 1, k + 1): return True
      if DFS(stone + k - 1, k - 1): return True
      if DFS(stone + k, k): return True
        
      return False
    
    return DFS(0, 0)

class Solution:
  def canCross(self, stones):
    last = stones[-1]
    stoneSet = set(stones)
    DP = {}
    
    def DFS(stone, k):
      if stone == last: return True
      if stone not in stoneSet: return False
      if (stone, k) in DP: return DP[(stone, k)]
      DP[(stone, k)] = False
    
      if DFS(stone + k + 1, k + 1): return True
      if DFS(stone + k - 1, k - 1): return True
      if DFS(stone + k, k): return True
      
      return False
    
    return DFS(0, 0)
  
def runSolution():
  solution = Solution()
  print(solution.canCross(stones = [0,1,3,5,6,8,12,17]))
  print(solution.canCross(stones = [0,1,2,3,4,8,9,11]))
  pass
runSolution()