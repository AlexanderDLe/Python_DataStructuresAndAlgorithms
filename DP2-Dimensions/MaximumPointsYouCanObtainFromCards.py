'''

  1423. Maximum Points You Can Obtain from Cards
  
'''

from itertools import product

class SolutionDPInefficient:
  def maxScore(self, cardPoints, k):
    DP = {}
    
    def DFS(L, R, rounds):
      if (L, R) in DP: return DP[L,R]
      if L > R: return 0
      if rounds == 0: return 0
      
      # Pick left
      res = DFS(L + 1, R, rounds - 1) + cardPoints[L]
      
      # Pick right
      res = max(res, DFS(L, R - 1, rounds - 1) + cardPoints[R])
      
      DP[L, R] = res
      return res
    
    return DFS(0, len(cardPoints) - 1, k)

class Solution:
  def maxScore(self, cardPoints, k):
    if len(cardPoints) < k: return sum(cardPoints)
    currSum = 0
    
    for i in range(k):
      currSum += cardPoints[i]
    
    maxSum = currSum
    L = k - 1
    R = len(cardPoints) - 1
    
    for i in range(k):
      currSum -= cardPoints[L]
      currSum += cardPoints[R]
      L -= 1
      R -= 1
      maxSum = max(maxSum, currSum)

    return maxSum
    
    
    
  
def runSolution():
  solution = Solution()
  print(solution.maxScore(cardPoints = [1,2,3,4,5,6,1], k = 3))
  print(solution.maxScore(cardPoints = [2,2,2], k = 2))
  print(solution.maxScore(cardPoints = [9,7,7,9,7,7,9], k = 7))
  pass
runSolution()