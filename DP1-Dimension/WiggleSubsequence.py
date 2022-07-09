'''

  376. Wiggle Subsequence

'''

class SolutionRef:  
  def wiggleMaxLength(self, nums):
    if len(nums) == 0: return 0
    
    n = len(nums)
    up = down = 1
    
    for i in range(1, n):
      prev, curr = nums[i - 1], nums[i]
      
      if curr < prev: down = up + 1
      if curr > prev: up = down + 1
    
    return max(up, down)   
    
    
class Solution:  
  def wiggleMaxLength(self, nums):
    if len(nums) == 0: return 0
    up = down = 1
    
    for i in range(1, len(nums)):
      prev, curr = nums[i - 1], nums[i]
      
      if curr < prev:
        down = up + 1
        
      if curr > prev:
        up = down + 1
      
    
    return max(up, down)
    
  
def runSolution():
  solution = Solution()
  print(solution.wiggleMaxLength([1,7,4,9,2,5]))
  print(solution.wiggleMaxLength([1,17,5,10,13,15,10,5,16,8]))
  print(solution.wiggleMaxLength([1,2,3,4,5,6,7,8,9]))
  pass
runSolution()