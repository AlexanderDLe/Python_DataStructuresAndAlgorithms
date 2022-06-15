'''

  1235. Maximum Profit in Job Scheduling

'''

from functools import cache


class SolutionRef:
  def jobScheduling(self, startTime, endTime, profit):
    n = len(startTime)
    jobs = sorted(list(zip(startTime, endTime, profit)))
    
    @cache
    def DFS(index):
      if index == n: return 0
      ans = DFS(index + 1) # Choice 1. Don't pick
      
      for j in range(index + 1, n + 1):
        if j == n or jobs[j][0] >= jobs[index][1]:
          print(index, j)
          ans = max(ans, DFS(j) + jobs[index][2]) # Choice 2: Pick
          break
      
      return ans
    
    return DFS(0)
  
  
class Solution:
  def jobScheduling(self, startTime, endTime, profit):
    jobs = list(zip(startTime, endTime, profit))
    jobs.sort()
    n = len(jobs)
    DP = {}
    
    def DFS(index):
      if index in DP: return DP[index]
      if index == n: return 0

      # Don't take
      res = DFS(index + 1)
      
      # Take
      res = max(res, jobs[index][2])
      
      # DFS over next possibilities
      for i in range(index + 1, n):
        if jobs[i][0] < jobs[index][1]: continue
        res = max(res, DFS(i) + jobs[index][2])
        
      DP[index] = res
      return res
    
    result = DFS(0)
    return result



def runSolution():
  solution = Solution()
  print(solution.jobScheduling(startTime = [1,2,3,3], endTime = [3,4,5,6], profit = [50,10,40,70]))
  print(solution.jobScheduling(startTime = [1,2,3,4,6], endTime = [3,5,10,6,9], profit = [20,20,100,70,60]))
  print(solution.jobScheduling(startTime = [1,1,1], endTime = [2,3,4], profit = [5,6,4]))
  pass
runSolution()
