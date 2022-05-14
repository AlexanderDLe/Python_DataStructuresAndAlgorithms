'''

  90. Subsets II

  1   2   2   4
  ^
  [], [1]

  1   2   2   4
      ^ 
  [], [1], [1,2], [2]

  1   2   2   4
          ^  <--- Duplicate: append to only most recent additions
          
  [], [1], [1,2], [2], [1,2,2], [2,2]
              ^    ^
              Previously added
'''

class Solution:
  def subsetsWithDup(self, nums):
    nums.sort()
    result = [[]]
    prevAdded = 0
    
    for i, curr in enumerate(nums):
      prev = nums[i - 1] if i > 0 else float('inf')
      start = 0 if curr != prev else len(result) - prevAdded
      prevAdded = 0
      res = []
      
      for j in range(start, len(result)):
        prevAdded += 1
        res.append(result[j] + [curr])
      
      result.extend(res)
    
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.subsetsWithDup(nums = [1,2,2]))
  print(solution.subsetsWithDup(nums = [1,2,2,4]))
  print(solution.subsetsWithDup(nums = [0]))
  pass
runSolution()
