'''

  1980. Find Unique Binary String

'''

class Solution:
  def findDifferentBinaryString(self, nums):
    n = len(nums[0])
    nums = set(nums)
    res = ''
    
    def backtrack(index, curr):
      nonlocal res

      if res != '': return
      if index == n:
        s = ''.join(curr)
        if s not in nums: res = s
        return
      
      curr.append('0')
      backtrack(index + 1, curr)
      curr[index] = '1'
      backtrack(index + 1, curr)
      curr.pop()
      
    backtrack(0, [])
    return res

    
  
  
def runSolution():
  solution = Solution()
  print(solution.findDifferentBinaryString(nums = ["0"]))
  # print(solution.findDifferentBinaryString(nums = ["01","10"]))
  # print(solution.findDifferentBinaryString(nums = ["00","01"]))
  # print(solution.findDifferentBinaryString(nums = ["111","011","001"]))
  pass
runSolution()
