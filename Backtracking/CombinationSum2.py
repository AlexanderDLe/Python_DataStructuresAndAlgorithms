'''

  40. Combination Sum II

'''

class Solution:
  def combinationSum2(self, candidates, target):
    candidates.sort()
    n = len(candidates)
    result = []
    
    def backtrack(index, sum, res):
      if sum == target: result.append(res.copy())
      if sum >= target or index == n or candidates[index] > target: return
      
      
      res.append(candidates[index])
      backtrack(index + 1, sum + candidates[index], res)
      res.pop()
      
      while index < n - 1 and candidates[index] == candidates[index + 1]:
        index += 1
      backtrack(index + 1, sum, res)
        
    backtrack(0, 0, [])
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.combinationSum2(candidates = [10,1,2,7,6,1,5], target = 8))
  print(solution.combinationSum2(candidates = [2,5,2,1,2], target = 5))
  pass
runSolution()
