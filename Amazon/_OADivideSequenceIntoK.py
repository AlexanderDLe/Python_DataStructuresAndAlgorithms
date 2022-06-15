'''

  QUESTION:
  Mike is the naughtiest student in the class. 
  So, Bob, his class teacher, gave him a sequence A containing only 0 and 1.
  
  Bob wanted Mike to divide the sequence in such a way that each division must 
  give the sum exactly K.
  
  To increase Mike's punishment, Bob wanted that Mike should find all the unique 
  divisions that follow the given conditions.

  Notes:
  The count of divisions can be huge. So, Output the count mod 109+7.
  The whole array is not considered as a division.

  Determine all unique divisions such that each segment has a sum equal 
  to exactly K. If there are no new divisions possible, return 0.

  ---------------------------------------------------------------------
  
  Example 1

  N = 18, K = 4
  A = 0 1 1 1 1 0 1 0 1 1 0 1 0 1 1 1 1 0
  Approach

  1st division: 0 1 1 1 1 - 0 1 0 1 1 0 1 0 - 1 1 1 1 0
  2nd division: 0 1 1 1 1 0 - 1 0 1 1 0 1 0 - 1 1 1 1 0
  3rd division: 0 1 1 1 1 - 0 1 0 1 1 0 1 - 0 1 1 1 1 0
  4th division: 0 1 1 1 1 0 - 1 0 1 1 0 1 - 0 1 1 1 1 0
  
  Mike can form 4 diffrent sequences.
  
  ---------------------------------------------------------------------
  
  Example-2:
  Given

  N = 3
  K = 1
  A = 0 1 0
  Approach

  You cannot get any new divisions. Hence, print 0.
  
  ---------------------------------------------------------------------
  
  Strategy

  N = 18, K = 4
  A = 0 1 1 1 1 0 1 0 1 1 0 1 0 1 1 1 1 0
        |     |   |         |   |     |
  
  First, check if totalOnes are able to be split into groups of k.
  
  totalOnes = 12
  12 /4 = 3 groups of 4 1s
  
  Find gaps between the groups.
  3 groups means 2 gaps.
  
  group1| gap1 | group2 | gap2 | group3
            ^               ^
            
  We basically want to return all the variations of the gaps.
  The gap variations are what determine how the groups can be split.
  
  Ex:
  
  1|1    <--- No variation
  
  1|0|1  <--- 2 variations
                10|1
                1|01
                
  1|00|1  <--- 3 variations
                100|1
                10|01
                1|001
                
  Variations = numberOfZeroes + 1
  
  ---------------------------------

  1. Basically get the gaps between groups.
     Store the gaps in gapStart and gapEnd to find
     the difference.
     
  2. Return the product of all the gaps.
'''

from collections import defaultdict

class Solution:
  def func(self, n, k, nums):
    totalOnes = nums.count(1)
    if totalOnes/k % 1: return 0
    if totalOnes/k < 2: return 0
    
    gapStart, gapEnd = self.getGaps(k, nums)
    result = gapEnd[0] - gapStart[0]
    
    for i in range(1, len(gapEnd)):
      diff = gapEnd[i] - gapStart[i]
      
      result *= diff
    
    return result
    
  
  def getGaps(self, k, nums):
    gapStart, gapEnd = [], []
    count = 0
    
    for i, num in enumerate(nums):
      count += num
      
      if num and count == 1 and len(gapStart) > 0:
        gapEnd.append(i)
        
      if count == k:
        gapStart.append(i)
        count = 0
    
    return gapStart, gapEnd
    
    
    
  
def runSolution():
  solution = Solution()
  # print(solution.func(
  #   n = 18, k = 4, nums = [0,1,1,1,1,0,1,0,1,1,0,1,0,1,1,1,1,0]))
  # print(solution.func(
  #   n = 3, k = 1, nums = [0,1,0]))
  # print(solution.func(
  #   n = 3, k = 2, nums = [1,1,0,1,1,0,0,1,1]))
  print(solution.func(
    n = 3, k = 1, nums = [1,1,0,1,1,0,0,1,1]))
  pass
runSolution()