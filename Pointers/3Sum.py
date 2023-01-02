'''

  15. 3Sum

'''

class SolutionRef:
  def threeSum(self, nums):
    nums.sort()
    n = len(nums)
    result = []
    
    L = 0
    while L < n - 2:
      M, R = L + 1, n - 1
      
      while M < R:
        sum = nums[L] + nums[M] + nums[R]
        
        if sum == 0: 
          result.append([nums[L], nums[M], nums[R]])
          while M < R and nums[M] == nums[M + 1]: M += 1
          while R > M and nums[R] == nums[R - 1]: R -= 1
          M += 1
          R -= 1
        elif sum > 0:
          R -= 1
        else:
          M += 1      
      
      while L < n - 2 and nums[L] == nums[L + 1]: L += 1
      L += 1
    
    return result
  

class Solution:
  
  '''
  
    Time Complexity
    O(n^2) to iterate twice over
    
    Space Complexity
    O(n^2) to potentially store each iteration
  
  '''
  
  def threeSum(self, nums):
    nums.sort()
    result = []
    n = len(nums)
    L = 0
    
    while L < n - 2:
      M, R = L + 1, n - 1
      
      while M < R:
        sum = nums[L] + nums[M] + nums[R]
        
        if sum == 0:
          result.append([nums[L], nums[M], nums[R]])
          while M < R and nums[M] == nums[M + 1]: M += 1
          while M < R and nums[R] == nums[R - 1]: R -= 1
          M += 1
          R -= 1
        elif sum < 0:
          M += 1
        elif sum > 0:
          R -= 1
      
      while L < n - 2 and nums[L] == nums[L + 1]: L += 1
      L += 1
    
    return result
  
def runSolution():
  solution = Solution()
  print(solution.threeSum(nums = [-1,0,1,2,-1,-4]))
  pass
runSolution()
