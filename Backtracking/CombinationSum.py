'''

  39. Combination Sum

'''

class Solution:
  def combinationSum(self, candidates, target):
    result = []
    
    def backtrack(index, sum, res):
      if sum == target: 
        result.append(res.copy())
        return
      if index >= len(candidates) or sum > target: return
      
      res.append(candidates[index])
      backtrack(index, sum + candidates[index], res)
      res.pop()
      
      backtrack(index + 1, sum, res)
      
        
    backtrack(0, 0, [])
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.combinationSum(candidates = [2,3,6,7], target = 7))
  print(solution.combinationSum(candidates = [2,3,5], target = 8))
  pass
runSolution()
