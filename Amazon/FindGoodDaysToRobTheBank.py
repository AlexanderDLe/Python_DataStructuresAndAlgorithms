'''

  2100. Find Good Days to Rob the Bank
  
'''

class Solution:
  def goodDaysToRobBank(self, security, time):
    n = len(security)
    fromLeft, fromRight = [0] * n, [0] * n
    
    for i in range(1, n):
      if security[i] >= security[i - 1]: 
        fromLeft[i] = fromLeft[i - 1] + 1
      
      if security[n - i - 1] >= security[n - i]:
        fromRight[n - i - 1] = fromRight[n - i] + 1
    
    result = []
    for i in range(time, n - time):
      if fromRight[i - time] >= time and fromLeft[i + time] >= time:
        result.append(i)
    
    return result
    
    
  
def runSolution():
  solution = Solution()
  print(solution.goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
  print(solution.goodDaysToRobBank(security = [1,1,1,1,1], time = 0))
  print(solution.goodDaysToRobBank(security = [1,2,3,4,5,6], time = 2))
  pass
runSolution()