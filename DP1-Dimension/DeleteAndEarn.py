'''

  740. Delete and Earn

'''

from itertools import groupby


class Solution:
  def deleteAndEarn(self, nums):
    arr = self.buildArray(nums)
    n = len(arr)
    
    if n == 0: return 0
    if n == 1: return arr[0]
    
    far = arr[0]
    close = arr[1]
    
    for i in range(2, n):
      temp = far
      far = close
      close = max(close, temp + arr[i])
    
    return close
  
  def buildArray(self, nums):
    nums.sort()
    arr = [0] * (max(nums) + 1)
    
    for num in nums:
      arr[num] += num
      
    return arr
  

def runSolution():
  solution = Solution()
  print(solution.deleteAndEarn(nums = [3,4,2]))
  print(solution.deleteAndEarn(nums = [2,2,3,3,3,4]))
  print(solution.deleteAndEarn(nums = [4,10,10,8,1,4,10,9,7,6]))
  pass
runSolution()