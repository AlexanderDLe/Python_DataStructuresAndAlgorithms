'''

  78. Subsets

'''

class Solution:
  def subsets(self, nums):
    result = []
    
    def backtrack(index, res):
      if index == len(nums):
        result.append(res.copy())
        return
      
      backtrack(index + 1, res)
      
      res.append(nums[index])
      backtrack(index + 1, res)
      res.pop()
    
    backtrack(0, [])
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.subsets(nums = [1,2,3]))
  print(solution.subsets(nums = [1,2,3,4]))
  print(solution.subsets(nums = [0]))
  pass
runSolution()
