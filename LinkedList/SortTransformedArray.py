'''

  360. Sort Transformed Array

'''

class Solution:
  def sortTransformedArray(self, nums, a, b, c):
    arr = list(map(lambda x: (a*(x*x)+(b*x)+c), nums))
    isNegative = a < 0
    p   = 0 if isNegative else len(arr) - 1
    itr = 1 if isNegative else -1
    L, R = 0, len(arr) - 1
    
    while L <= R:
      if isNegative:
        if arr[L] < arr[R]: 
          nums[p] = arr[L]
          L += 1
        else:
          nums[p] = arr[R]
          R -= 1
          
      else:
        if arr[L] > arr[R]:
          nums[p] = arr[L]
          L += 1
        else:
          nums[p] = arr[R]
          R -= 1
      
      p += itr
    
    return nums
      
  

def runSolution():
  solution = Solution()
  print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = 1, b = 3, c = 5))
  print(solution.sortTransformedArray(nums = [-4,-2,2,4], a = -1, b = 3, c = 5))
  pass
runSolution()

