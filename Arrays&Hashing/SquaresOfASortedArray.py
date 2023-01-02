'''

  977. Squares of a Sorted Array
  
'''

class Solution:
  
  '''

    Time Complexity:
    O(n) to iterate through all numbers
    
    Space Complexity
    O(n) to store all squared nums and result.
  
  '''
  
  def sortedSquares(self, nums):
    squared = list(map(lambda x: x*x, nums))
    
    n = len(nums)
    result = [0] * n
    curr = n - 1
    L, R = 0, n - 1
    
    while L <= R:
      if squared[L] > squared[R]:
        result[curr] = squared[L]
        L += 1
      else:
        result[curr] = squared[R]
        R -= 1
      
      curr -= 1
      
    return result
    
      
  
def runSolution():
  solution = Solution()
  print(solution.sortedSquares(nums = [-4,-1,0,3,10]))
  print(solution.sortedSquares(nums = [-7,-3,2,3,11]))
  pass
runSolution()
