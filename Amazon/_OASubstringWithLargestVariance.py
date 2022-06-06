'''

  2272. Substring With Largest Variance

'''



from itertools import combinations


class Solution:
  def largestVariance(self, s):
    def kadanes(nums):
      ans = -float('inf')
      runningSum, seen = 0, False
      print(nums)
      for x in nums:
        if x < 0: seen = True
        runningSum += x
        
        if seen: ans = max(ans, runningSum)
        else   : ans = max(ans, runningSum - 1)
        
        print('pre', seen, runningSum, ans)
        # Reset if negative
        if runningSum < 0:
          runningSum = 0
          seen = False
        print('pos', seen, runningSum, ans)

      print(ans)
      return ans
    
    a, res = ''.join(set(s)), 0
    
    for i in range(len(a) - 1):
      for j in range(i + 1, len(a)):
        arr, x, y = [], a[i], a[j]
        print(x, y)
        for char in s:
          if   char == x: arr.append(1)
          elif char == y: arr.append(-1)
        
        res = max(res, kadanes(arr), kadanes([-x for x in arr]))
    
    return res
          
      

def runSolution():
  solution = Solution()
  # print(solution.largestVariance(s = "abcde"))
  # print(solution.largestVariance(s = "aababbb"))
  print(solution.largestVariance(s = "iaa"))
  pass
runSolution()
