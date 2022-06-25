'''

  402. Remove K Digits

'''


class Solution:
  def dailyTemperatures(self, num, k):
    stack = []
    
    for digit in num:
      while k > 0 and stack and stack[-1] > digit:
        k -= 1
        stack.pop()
      stack.append(digit)
      
    stack = stack[:len(stack) - k]
    res = ''.join(stack)
    return str(int(res)) if res else '0'
  
def runSolution():
  solution = Solution()
  print(solution.dailyTemperatures(num = "1432219", k = 3))
  print(solution.dailyTemperatures(num = "10200", k = 1))
  print(solution.dailyTemperatures(num = "10", k = 2))
  pass
runSolution()
