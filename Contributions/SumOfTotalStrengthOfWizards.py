'''

  2281. Sum of Total Strength of Wizards
  https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2062017/C%2B%2B-prefix-%2B-monotonic-stack-O(N)-solution-with-thought-process
  

  Prefix sums to get sums of group
  monotonic stack to determine NGE/PGE group boundaries

        1  3  1  2
  PLE  -1  0  0  2
  NLE   4  2  4  4
  sum   1  4  5  7
  
  
  
'''


from itertools import accumulate


class SolutionRef:
  def totalStrength(self, strength):
    mod = 10 ** 9 + 7
    n = len(strength)

    # next small on the left
    PLE = [-1] * n
    stack = []
    for i in range(n):
      while stack and strength[i] < strength[stack[-1]]: stack.pop()
      if stack: PLE[i] = stack[-1]
      stack.append(i)
    
    # next small on the right
    NLE = [n] * n
    stack = []
    for i in range(n - 1, -1, -1):
      while stack and strength[i] <= strength[stack[-1]]: stack.pop()
      if stack: NLE[i] = stack[-1]
      stack.append(i)
      
    print(PLE, NLE)
    
    # for each A[i] as minimum, calculate sum
    res = 0
    acc = list(accumulate(accumulate(strength), initial = 0))
    print(acc)
    
    for i in range(n):
      l, r = PLE[i], NLE[i]
      
      lacc = acc[i] - acc[max(l, 0)]
      racc = acc[r] - acc[i]
      ln, rn = i - l, r - i
      print('___________')
      print(i)
      print('L:', l, lacc, ln)
      print('R:', r, racc, rn)
      print(strength[i] * (racc * ln - lacc * rn))
      res += strength[i] * (racc * ln - lacc * rn)
      
    return res % mod
  

class Solution:
  def totalStrength(self, strength):
    n = len(strength)
    PLE, NLE = self.init(strength)
    print(PLE, NLE)
    totalStrength = 0
    
    acc = list(accumulate(accumulate(strength), initial = 0))
    print(acc)
    for i in range(n):
        l, r = PLE[i], NLE[i]
        lacc = acc[i] - acc[max(l, 0)]
        racc = acc[r] - acc[i]
        ln, rn = i - l, r - i
        totalStrength += strength[i] * (racc * ln - lacc * rn)
    
    return totalStrength
  

  def init(self, strength):
    n = len(strength)
    PLE = [-1] * n
    NLE = [n] * n
    
    stack = []
    for i in range(n):
      str = strength[i]
      
      while stack and str <= strength[stack[-1]]: stack.pop()
      if stack: PLE[i] = stack[-1]
      stack.append(i)
    
    stack = []
    for i in range(n - 1, -1, -1):
      str = strength[i]
      
      while stack and str < strength[stack[-1]]: stack.pop()
      if stack: NLE[i] = stack[-1]
      stack.append(i)
    
    return PLE, NLE
  
def runSolution():
  solution = SolutionRef()
  print(solution.totalStrength([1,3,1,2]))
  # print(solution.totalStrength(strength = [5,4,6]))
  pass
runSolution()