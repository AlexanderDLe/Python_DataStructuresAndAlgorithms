'''

  1554. Strings Differ by One Character
  
'''

class SolutionRef:
  def differByOne(self, dict):
    n, m = len(dict), len(dict[0])
    hashes = [0] * n
    MOD = 10 ** 11 + 7
    
    for i in range(n):
      for j in range(m):
        char = dict[i][j]
        hashes[i] = 26 * hashes[i] + self.code(char)
    print(hashes)
    
    base = 1
    for j in range(m - 1, -1, -1):
      seen = set()
      for i in range(n):
        char = dict[i][j]
        newH = (hashes[i] - base * self.code(char))
        
        if newH in seen: return True        
        seen.add(newH)      
        
      base = 26 * base
  
  def code(self, char):
    return ord(char) - ord('a')
      
    
class Solution:
  def differByOne(self, dict):
    wordLen, charLen = len(dict), len(dict[0])
    hashes = [0] * wordLen
    
    for i in range(wordLen):
      for j in range(charLen):
        char = dict[i][j]
        hashes[i] = (26 * hashes[i]) + self.code(char)
        
    base = 1
    for j in range(charLen - 1, -1, -1):
      seen = set()
      
      for i in range(wordLen):
        char = dict[i][j]
        newH = hashes[i] - (base * self.code(char))
        
        if newH in seen: return True
        seen.add(newH)
      
      base *= 26
    
    return False
        
  def code(self, char):
    return ord(char) - ord('a')
      
    
    
  
def runSolution():
  solution = Solution()
  print(solution.differByOne(dict = ["abcd","acbd", "aacd"]))
  print(solution.differByOne(dict = ["ab","cd","yz"]))
  print(solution.differByOne(dict = ["abcd","cccc","abyd","abab"]))
  pass
runSolution()
