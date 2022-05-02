'''

  217. Contains Duplicate

'''


class Solution:
  def containsDuplicate(self, nums):
    seen = set()
    for num in nums:
      if num in seen: return True
      seen.add(num)
    return False
  
def runSolution():
  solution = Solution()
  print(solution.containsDuplicate([1,2,3,1]))
  print(solution.containsDuplicate([1,2,3,4]))
  print(solution.containsDuplicate([1,1,1,3,3,4,3,2,4,2]))
  pass
runSolution()
