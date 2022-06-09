'''

  Appeared for Amazon OA recently, for internship role. This was the question
  Given an Array contaning N integers find the prefix of the M times.
  
  --------------------------------------------------
  
  Example 
  N=3
  M=2
  
  arr = 1 2 3
    1 = 1 3 6
    2 = 1 4 10
  O/P-> 1 4 10
  
  ---------------------------------------------------
  
  N=5
  M=3
  
  Arr = 1 2  3  4  5
    1 = 1 3  6 10 15
    2 = 1 4 10 20 35
    3 = 1 5 15 35 70
    
  O/P = 1 5 15 35 70
  
  While converting to prefix sums, do the operation modulo 10^9 +7.
  
  1<=N<=1000
  1<=M,arr[i]<=10^9
'''

import heapq

class Solution:
  def func(self, n, m):
    DP = [[0]*n for _ in range(m + 1)]
    
    for row in DP: row[0] = 1
    for i in range(n): DP[0][i] = i + 1
    
    for row in range(1, m + 1):
      for col in range(1, n):
        DP[row][col] = DP[row - 1][col] + DP[row][col - 1]
        
    return DP[-1]
      
  
def runSolution():
  solution = Solution()
  print(solution.func(3, 2))
  # print(solution.func(2, 3))
  pass
runSolution()