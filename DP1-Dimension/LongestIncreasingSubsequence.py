'''

  300. Longest Increasing Subsequence

    0   1   0   3   2   3
DP  1   2   1   1   1   1


'''

class Solution:
  def lengthOfLIS(self, nums):
    if not nums: return 0
    
    n = len(nums)
    DP = [1] * n
    DP[0] = 1
    result = 1
    
    for i in range(1, n):
      for j in range(i - 1, -1, -1):
        if nums[j] < nums[i]: 
          DP[i] = max(DP[i], DP[j] + 1)
          result = max(result, DP[i])
    
    return result

def runSolution():
  solution = Solution()
  print(solution.lengthOfLIS(nums = [10,9,2,5,3,7,101,18]))
  print(solution.lengthOfLIS(nums = [0,1,0,3,2,3]))
  print(solution.lengthOfLIS(nums = [7,7,7,7,7,7,7]))
  pass
runSolution()