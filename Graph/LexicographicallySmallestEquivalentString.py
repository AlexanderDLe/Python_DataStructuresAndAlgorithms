'''

  1061. Lexicographically Smallest Equivalent String

'''

class UnionFind:
  def __init__(self, s1, s2):
    self.roots = {}
    for char in s1: self.roots[char] = char
    for char in s2: self.roots[char] = char
    
  def find(self, char):
    roots = self.roots
    if char != roots[char]:
      roots[char] = self.find(roots[char])
    return roots[char]
  
  def union(self, x, y):
    xRoot, yRoot = self.find(x), self.find(y)
    
    if ord(xRoot) < ord(yRoot): 
      self.roots[yRoot] = xRoot
    else: 
      self.roots[xRoot] = yRoot

class Solution:
  def smallestEquivalentString(self, s1, s2, baseStr):
    UF = UnionFind(s1, s2)
    
    for charA, charB in zip(s1, s2):
      UF.union(charA, charB)
      
    result = ''
    for char in baseStr:
      if char not in UF.roots: result += char
      else: result += UF.find(char)
    
    return result
  

def runSolution():
  solution = Solution()
  # print(solution.smallestEquivalentString(s1 = "parker", s2 = "morris", baseStr = "parser"))
  # print(solution.smallestEquivalentString(s1 = "hello", s2 = "world", baseStr = "hold"))
  # print(solution.smallestEquivalentString(s1 = "leetcode", s2 = "programs", baseStr = "sourcecode"))
  print(solution.smallestEquivalentString(
    "dfedffbbb",
    "adcabdbea",
    "c"
  ))
  pass
runSolution()