'''

  46. Permutations

'''

class Solution:
  def permute(self, nums):
    n = len(nums)
    result = []
    
    def backtrack(index):
      if index == n:
        result.append(nums.copy())
        return
    
      for i in range(index, n):
        nums[i], nums[index] = nums[index], nums[i]
        backtrack(index + 1)
        nums[i], nums[index] = nums[index], nums[i]
    
    backtrack(0)
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.permute(nums = [1,2,3]))
  print(solution.permute(nums = [1,2,3,4]))
  print(solution.permute(nums = [0]))
  print(solution.permute(nums = [0, 1]))
  pass
runSolution()
