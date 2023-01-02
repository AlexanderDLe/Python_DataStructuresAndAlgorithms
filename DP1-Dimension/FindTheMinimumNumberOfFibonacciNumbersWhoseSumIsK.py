'''

  1414. Find the Minimum Number of Fibonacci Numbers Whose Sum Is K

'''

class Solution:
  def findMinFibonacciNumbers(self, k):
    ans = 0
    fibs = [1, 1]
    
    while fibs[-1] <= k:
      fibs.append(fibs[-1] + fibs[-2])
    
    for i in range(len(fibs) - 1, -1, -1):
      if fibs[i] <= k:
        ans += 1
        k -= fibs[i]
      if k == 0:
        break
      
    return ans
    
    
  
def runSolution():
  solution = Solution()
  # print(solution.findMinFibonacciNumbers(k = 7))
  # print(solution.findMinFibonacciNumbers(k = 10))
  # print(solution.findMinFibonacciNumbers(k = 19))
  print(solution.findMinFibonacciNumbers(k = 16))
  pass
runSolution()