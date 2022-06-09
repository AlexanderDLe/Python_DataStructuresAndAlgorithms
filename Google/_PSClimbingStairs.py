'''
  
  As the title says, give all combinations in order to reach step 'N' with only allowed leap sizes of 1 and 2

  Ex 1: N = 1
  ['1']

  Ex 2: N = 2
  ['11', '2']

  Ex 3: N = 3
  ['111', '21', '12']

  Ex 3: N = 4
  ['1111', '112, '121', '211', '22']

  Answer: 
  Add '1' to all possible solutions to N-1'th level 
  add '2' to all possible solutions to N-2'th level 
  Combine both to get all possible solutions to N'th level

'''

class Solution:
  def main(self, n):
    prev2 = ['1']
    prev1 = ['11', '2']
    
    if n == 0: return []
    if n == 1: return prev2
    if n == 2: return prev1
    
    for _ in range(3, n + 1):
      curr = []
      for item in prev2: curr.append(item + '2')
      for item in prev1: curr.append(item + '1')
      prev2 = prev1
      prev1 = curr
    
    return curr

  
def runSolution():
  solution = Solution()
  print(solution.main(3))
  print(solution.main(5))
  pass
runSolution()