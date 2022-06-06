'''

  1567. Maximum Length of Subarray With Positive Product


elements      :   9    5    8    2    -6    4    -3    0    2    -5    15    10    -7    9    -2
positive_len  :   1    2    3    4     0    1     7    0    1     0     1     2     5    6     5
negative_len  :   0    0    0    0     5    6     2    0    0     2     3     4     3    4     7



elements      :   9    5    -8    -2    -6    -4    -3    1    2    -5    15    10    -7    9    -2
positive_len  :   1    2     0     4     2     6     4    5    6    10    11    12    10   11    15
negative_len  :   0    0     3     1     5     3     7    8    9     7     8     9    13   14    12

elements      :  -1    2    -5
positive_len  :   0    1     3
negative_len  :   1    2     2
  
'''


class Solution:
  def getMaxLen(self, nums):
    ans = positive = negative = 0
    
    for num in nums:
      if num == 0:
        positive = 0
        negative = 0
        continue
      
      if num > 0:
        positive += 1
        negative = 0 if negative == 0 else negative + 1
        
      if num < 0:
        temp = positive
        positive = 0 if negative == 0 else negative + 1
        negative = temp + 1
        
      ans = max(ans, positive)
      print('P:', positive, '-- N:', negative)
        
    return ans

  
def runSolution():
  solution = Solution()
  # print(solution.getMaxLen(nums = [1,-2,-3,4]))
  # print(solution.getMaxLen(nums = [0,1,-2,-3,-4]))
  # print(solution.getMaxLen(nums = [-1,-2,-3,0,1]))
  # print(solution.getMaxLen(nums = [9,5,8,2,-6,4,-3,0,2,-5,15,10,-7,9,-2]))
  print(solution.getMaxLen(nums = [9,5,-8,-2,-6,-4,-3,1,2,-5,15,10,-7]))
  print(solution.getMaxLen(nums = [-1,2,-5]))
  pass
runSolution()
