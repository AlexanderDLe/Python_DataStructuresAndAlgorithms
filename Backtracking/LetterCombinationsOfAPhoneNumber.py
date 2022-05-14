'''

  17. Letter Combinations of a Phone Number
  
'''

class Solution:
  phoneMap = {
    '1': [],
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
    '0': [],
  }
  
  def letterCombinations(self, digits):
    if not digits: return []
    
    result = ['']
    
    for digit in digits:
      chars = self.phoneMap[digit]
      res = []
      
      for prev in result:
        for item in chars:
          res.append(prev + item)
      
      result = res
    
    return result
  
  
def runSolution():
  solution = Solution()
  print(solution.letterCombinations(digits = "23"))
  print(solution.letterCombinations(digits = ""))
  print(solution.letterCombinations(digits = "2"))
  pass
runSolution()
