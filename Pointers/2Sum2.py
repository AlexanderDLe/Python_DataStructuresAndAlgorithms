'''

  167. Two Sum II - Input Array is Sorted

'''

class Solution:
  def twoSum(self, numbers, target):
    L, R = 0, len(numbers) - 1
    
    while L < R:
      sum = numbers[L] + numbers[R]
      if sum == target: return [L + 1, R + 1]
      
      if sum > target: R -= 1
      else           : L += 1
      
    return []
  
def runSolution():
  solution = Solution()
  print(solution.twoSum(numbers = [2,7,11,15], target = 9))
  print(solution.twoSum(numbers = [2,3,4], target = 6))
  pass
runSolution()
