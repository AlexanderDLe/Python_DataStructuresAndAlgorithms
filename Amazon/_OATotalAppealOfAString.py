'''

  2262. Total Appeal of A String

  a b b c a

'''


from collections import defaultdict


class SolutionRef1:
  def appealSum(self, s):
    last = {}
    res = 0
    for i,c in enumerate(s):
      last[c] = i + 1
      res += sum(last.values())
      print(res, last.values())
    return res

class Solution:
  def appealSum(self, s):
    last = defaultdict(lambda: -1)
    res, n = 0, len(s)
    
    for i, c in enumerate(s):
      print(f'{c, i, last[c], n}')
      print(i - last[c], n - i, (i - last[c]) * (n - i))
      res += (i - last[c]) * (n - i)
      last[c] = i
        
    return res
    
  
def runSolution():
  solution = Solution()
  print(solution.appealSum(s = "abbca"))
  # print(solution.appealSum(s = "code"))
  pass
runSolution()
