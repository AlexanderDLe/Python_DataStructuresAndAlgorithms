'''

  737. Sentence Similarity II

'''

from itertools import product


class UnionFind:
  def __init__(self, similarPairs):
    self.roots = {}
    
    for x, y in similarPairs:
      if x not in self.roots: self.roots[x] = x
      if y not in self.roots: self.roots[y] = y
      self.union(x, y)
  
  def find(self, x):
    if x != self.roots[x]:
      self.roots[x] = self.find(self.roots[x])
    return self.roots[x]
  
  def union(self, x, y):
    rootX, rootY = self.find(x), self.find(y)
    # if rootX == rootY: return
    self.roots[rootX] = rootY
    
  def exists(self, x):
    return x in self.roots

class Solution:
  def areSentencesSimilarTwo(self, sentence1, sentence2, similarPairs):
    if len(sentence1) != len(sentence2): return False
    
    UF = UnionFind(similarPairs)
    
    for word1, word2 in zip(sentence1, sentence2):
      if word1 == word2: continue
      
      if UF.exists(word1) == False or UF.exists(word2) == False: return False
      if UF.find(word1) != UF.find(word2): return False
    
    return True
  
  

def runSolution():
  solution = Solution()
  # print(solution.areSentencesSimilarTwo(
  #   sentence1 = ["great","acting","skills"], 
  #   sentence2 = ["fine","drama","talent"], 
  #   similarPairs = [["great","good"],["fine","good"],["drama","acting"],["skills","talent"]]))
  print(solution.areSentencesSimilarTwo(
    sentence1 = ["I","love","leetcode"], 
    sentence2 = ["I","love","onepiece"], 
    similarPairs = [["manga","onepiece"],["platform","anime"],["leetcode","platform"],["anime","manga"]]))
  # print(solution.areSentencesSimilarTwo(
  #   sentence1 = ["I","love","leetcode"], 
  #   sentence2 = ["I","love","onepiece"], 
  #   similarPairs = [["manga","hunterXhunter"],["platform","anime"],["leetcode","platform"],["anime","manga"]]))
  pass
runSolution()
