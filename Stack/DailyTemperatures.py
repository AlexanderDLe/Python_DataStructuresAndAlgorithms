'''

  739. Daily Temperatures

'''


class Solution:
  def dailyTemperatures(self, temperatures):
    getTopTemp = lambda: temperatures[stack[-1]]
    stack = []
    n = len(temperatures)
    nextWarmer = [0] * n
    
    for i in range(n - 1, -1, -1):
      currTemp = temperatures[i]      
      while stack and currTemp >= getTopTemp(): stack.pop()
      
      if stack: nextWarmer[i] = stack[-1] - i        
      stack.append(i)
      
    return nextWarmer
  
def runSolution():
  solution = Solution()
  print(solution.dailyTemperatures(temperatures = [73,74,75,71,69,72,76,73]))
  print(solution.dailyTemperatures(temperatures = [30,40,50,60]))
  print(solution.dailyTemperatures(temperatures = [30,60,90]))
  pass
runSolution()
