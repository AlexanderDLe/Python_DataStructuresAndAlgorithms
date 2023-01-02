'''

  523. Continuous Subarray Sum

  ----------------------------------

  k = 6

   nums:  23   2   6   4   7
  total:   5   1   1   5

  rem: {
    0: -1
    5: 0
    1: 1
  }
   
'''

class SolutionRef:

  def checkSubarraySum(self, nums, k):
    # Start with -1 to take care of edge cases where we have not encountered a 0
    # yet but the distance from start should be at least 1
    remainder = {0: -1}
    moddedSum = 0

    for i, n in enumerate(nums):
      moddedSum += n
      moddedSum %= k
      
      # print(i, n, moddedSum)

      # Store the index for the modded sum
      if moddedSum not in remainder:
        remainder[moddedSum] = i
        # print(remainder)  
      
      # If the same modded value is the same and the distance between
      # is greater than 1, then we have found a continuous subarray
      elif i - remainder[moddedSum] > 1:
        # print(remainder)  
        return True
      

    return False

class Solution:

  '''
  
    Time Complexity
    O(n) Itereate through all numbers
    
    Space Complexity
    O(k) Store at most k values in map due to modding values by k
  
  '''

  def checkSubarraySum(self, nums, k):
    remaining = {0: -1}
    moddedSum = 0
    
    for i, num in enumerate(nums):
      moddedSum += num
      moddedSum %= k
      
      if moddedSum not in remaining:
        remaining[moddedSum] = i
        
      else:
        subarrayLength = i - remaining[moddedSum]
        if subarrayLength > 1: return True
        
    return False
  
def runSolution():
  solution = Solution()
  print(solution.checkSubarraySum([23,2,4,6,6], 7))
  print(solution.checkSubarraySum([23,2,4,6,7], 6))
  print(solution.checkSubarraySum([23,2,6,4], 6))
  print(solution.checkSubarraySum([23,2,6,4,7], 13))
  pass
runSolution()

