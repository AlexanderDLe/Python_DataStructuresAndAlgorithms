'''

  AlgoExpert Knapsack Problem

'''

from itertools import product


class Solution:
  def uniquePaths(self, items, capacity):
    n = len(items)
    DP = {}
    
    def DFS(index, prevWeight):
      if (index, prevWeight) in DP: return DP[index, prevWeight]
      if index == n: return 0, []
      
      itemWeight = items[index][0]
      res = 0
      itemsArr = []
      
      # Do not add item
      res = DFS(index + 1, prevWeight)
      
      # Add the item
      if itemWeight + prevWeight <= capacity:
        addedRes = DFS(index + 1, prevWeight + itemWeight)
        
        if addedRes + itemWeight > res:
          res = addedRes + itemWeight
          itemsArr.append(items[index][1])
        
      
      DP[index, prevWeight] = (res, itemsArr.copy())
      return res, itemsArr

    
    return DFS(0, 0)
  
  
def runSolution():
  solution = Solution()
  print(solution.uniquePaths([[1,2], [4,3], [5,6], [6,7]], 10))
  pass
runSolution()