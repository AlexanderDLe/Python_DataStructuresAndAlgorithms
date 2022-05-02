'''

  1248. Count Number of Nice Subarrays

'''


class SolutionContributions:
  def numberOfSubarrays(self, nums, k):
    n = len(nums)

    oddArr = self.buildOddArray(nums, n)
    result = 0
    L, R = 1, k
    
    while R < len(oddArr) - 1:
      left  = oddArr[L] - oddArr[L - 1]
      right = oddArr[R + 1] - oddArr[R]
      result += (left * right)
      
      L += 1
      R += 1
    
    return result
  
  def buildOddArray(self, nums, n):
    oddArr = [-1]
    for i, num in enumerate(nums): 
      if num % 2 == 1: oddArr.append(i)
      
    oddArr.append(n)
    return oddArr

def runSolution():
  solution = SolutionContributions()
  print(solution.numberOfSubarrays([1,1,2,1,1], k = 3))
  print(solution.numberOfSubarrays([2,4,6], k = 1))
  print(solution.numberOfSubarrays([2,2,2,1,2,2,1,2,2,2], k = 2))
  pass
runSolution()
