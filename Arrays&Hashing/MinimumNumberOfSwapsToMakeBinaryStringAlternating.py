'''

  1864. Minimum Number of Swaps to Make the Binary String Alternating

  10010
  10110
  10100
  10101
  
  z = 2
  o = 1
'''

class Solution:
  def minSwaps(self, s):
    zeroes = s.count('0')
    ones  = s.count('1')
    
    if abs(zeroes - ones) > 1: return -1
    
    if ones > zeroes: return self.solve(s, '1')
    if ones < zeroes: return self.solve(s, '0')
    return min(self.solve(s, '0'), self.solve(s, '1'))
    
  
  def solve(self, s, type):
    swaps = 0
    
    for char in s:
      if char != type: swaps += 1
      
      if   type == '0': type = '1'
      elif type == '1': type = '0'
    
    return swaps // 2
  
def runSolution():
  solution = Solution()
  print(solution.minSwaps(s = "111000"))
  print(solution.minSwaps(s = "010"))
  print(solution.minSwaps(s = "1110"))
  pass
runSolution()
