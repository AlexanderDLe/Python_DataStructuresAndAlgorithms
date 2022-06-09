'''

  179. Largest Number

'''

from functools import cmp_to_key


class Solution:
  def largestNumber(self, nums):
    def compare(a, b):
      AB = int(str(a) + str(b))
      BA = int(str(b) + str(a))
      return BA - AB
    
    nums.sort(key=cmp_to_key(compare))
    nums = list(map(lambda x: str(x), nums))
    
    s = ''.join(nums)
    return s if int(s) != 0 else '0'
  
def runSolution():
  solution = Solution()
  print(solution.largestNumber(nums = [10,2]))
  print(solution.largestNumber(nums = [4,2,1,3,6,8,9,5]))
  print(solution.largestNumber(nums = [3,30,34,5,9]))
  print(solution.largestNumber(nums = [0,0]))
  pass
runSolution()
