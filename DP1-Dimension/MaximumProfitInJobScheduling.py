'''

  1235. Maximum Profit in Job Scheduling

'''

from functools import cache


class Solution:
  def jobScheduling(self, startTime, endTime, profit):
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))
    print(jobs)
    
    @cache
    def DP(i):
      if i == n: return 0
      ans = DP(i + 1) # Choice 1. Don't pick
      
      for j in range(i + 1, n + 1):
        if j == n or jobs[j][0] >= jobs[i][1]:
          ans = max(ans, DP(j) + jobs[i][2]) # Choice 2: Pick
          print(i, j)
          break
      
      return ans
    
    return DP(0)
  
  
def runSolution():
  solution = Solution()
  # print(solution.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
  # print(solution.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
  print(solution.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
  pass
runSolution()
