'''

  368. Largest Divisible Subset

'''

class Solution:
  def largestDivisibleSubset(self, nums):
    nums.sort()
    result = [[num] for num in nums]
    
    for i in range(len(nums)):
      for j in range(i):
        if nums[i] % nums[j] != 0: continue
        
        if len(result[i]) < len(result[j]) + 1:
          result[i] = result[j] + [nums[i]]
    
    print(result)
    return max(result, key=len)
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.largestDivisibleSubset(nums = [1,2,3]))
  print(solution.largestDivisibleSubset(nums = [1,2,4,8]))
  print(solution.largestDivisibleSubset(nums = [4,5,8,12,16,20]))
  pass
runSolution()