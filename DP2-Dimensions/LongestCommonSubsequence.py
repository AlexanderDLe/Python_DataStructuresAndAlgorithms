'''

  1143. Longest Common Subsequence
  
    a  c  e
  a 1  
  b    1  1
  c    2 
  d       2
  e       1

'''

from itertools import product


class SolutionRef:
  def longestCommonSubsequence(self, text1, text2):
    DP = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
    
    for i in range(len(text1) - 1, -1, -1):
      for j in range(len(text2) - 1, -1, -1):
        if text1[i] == text2[j]:
          DP[i][j] = 1 + DP[i + 1][j + 1]
        else:
          DP[i][j] = max(DP[i][j + 1], DP[i + 1][j])
    
    return DP[0][0]


class Solution:
  def longestCommonSubsequence(self, text1, text2):
    DP = [[0]*(len(text2) + 1) for _ in range(len(text1) + 1)]
    
    for row in range(len(text1) - 1, -1, -1):
      for col in range(len(text2) - 1, -1, -1):
        if text1[row] == text2[col]:
          DP[row][col] = 1 + DP[row + 1][col + 1]
        else:
          DP[row][col] = max(DP[row + 1][col], DP[row][col + 1])
    
    return DP[0][0]
  
def runSolution():
  solution = Solution()
  print(solution.longestCommonSubsequence(text1 = "abcde", text2 = "ace"))
  print(solution.longestCommonSubsequence(text1 = "abc", text2 = "abc"))
  print(solution.longestCommonSubsequence(text1 = "abc", text2 = "def"))
  pass
runSolution()