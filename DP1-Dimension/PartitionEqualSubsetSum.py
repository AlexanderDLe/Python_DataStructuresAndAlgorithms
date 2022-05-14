'''

  416. Partition Equal Subset Sum
  
'''

class SolutionMine:
  def canPartition(self, nums):
    total = sum(nums)
    if total % 2: return False
    target = total / 2
    n = len(nums)
    
    DP = {}
    
    def DFS(index, curr):
      if index in DP and curr in DP[index]: return DP[index][curr]
      if curr == target: return True
      if curr > target or index >= n: return False
      
      withAdd = DFS(index + 1, curr + nums[index])
      withoutAdd = DFS(index + 1, curr)
      
      if index not in DP: DP[index] = {}
      DP[index][curr] = withAdd or withoutAdd
      
      return DP[index][curr]
    
    return DFS(0, 0)


class Solution:
  def canPartition(self, nums):
    total = sum(nums)
    if total % 2: return False
    target = total / 2
    seen = set([nums[0]])
    
    for i in range(1, len(nums)):
      num = nums[i]
      newSet = set(list(seen))
      
      for item in seen:
        newSet.add(num + item)
      
      seen = newSet
        
    if target in seen: return True
    return False

def runSolution():
  solution = Solution()
  print(solution.canPartition(nums = [1,5,11,5]))
  print(solution.canPartition(nums = [1,2,3,5]))
  pass
runSolution()