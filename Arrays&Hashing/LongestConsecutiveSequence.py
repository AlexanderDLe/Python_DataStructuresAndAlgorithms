'''

  217. Contains Duplicate

'''


class Solution:
  def longestConsecutive(self, nums):
    seen = set(nums)
    longest = 0
    
    for num in nums:
      if num - 1 in seen: continue
      currLength = 1
      
      while num + 1 in seen:
        currLength += 1
        num += 1
      
      longest = max(longest, currLength)
    
    return longest
  
def runSolution():
  solution = Solution()
  print(solution.longestConsecutive(nums = [100,4,200,1,3,2]))
  print(solution.longestConsecutive(nums = [0,3,7,2,5,8,4,6,0,1]))
  pass
runSolution()
