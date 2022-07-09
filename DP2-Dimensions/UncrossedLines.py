'''

  1035. Uncrossed Lines

'''

class SolutionTopDown:  
  def maxUncrossedLines(self, nums1, nums2):
    n1, n2 = len(nums1), len(nums2)
    DP = {}
    
    def DFS(i1, i2):
      if (i1, i2) in DP: return DP[i1, i2]
      if i1 == n1 or i2 == n2: return 0
      
      # Don't connect
      res = DFS(i1 + 1, i2)
      
      # Try all connections from q
      for i in range(i2, n2):
        if nums1[i1] != nums2[i]: continue
        res = max(res, 1 + DFS(i1 + 1, i + 1))

      DP[i1, i2] = res
      return res
    
    return DFS(0, 0)
    
class Solution:  
  def maxUncrossedLines(self, A, B):
    m, n = len(A), len(B)
    DP = [0] * (n + 1)
    
    print(DP)
    for i in range(m):
      for j in range(n)[::-1]:
        if A[i] == B[j]: DP[j + 1] = DP[j] + 1
      for j in range(n):
        DP[j + 1] = max(DP[j + 1], DP[j])
      print(DP)
      
    return DP[n]
    
  
def runSolution():
  solution = Solution()
  print(solution.maxUncrossedLines(A = [1,4,2], B = [1,2,4]))
  # print(solution.maxUncrossedLines(A = [2,5,1,2,5], B = [10,5,2,1,5,2]))
  # print(solution.maxUncrossedLines(A = [1,3,7,1,7,5], B = [1,9,2,5,1]))
  pass
runSolution()