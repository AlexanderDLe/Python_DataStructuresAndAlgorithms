'''

  1258. Synonymous Sentences

'''

from collections import defaultdict


class UnionFind:
  def __init__(self, synonyms):
    self.roots = {}
    
    # Init dict
    for wordA, wordB in synonyms:
      self.roots[wordA] = wordA
      self.roots[wordB] = wordB
      
    # Union synonyms
    for wordA, wordB in synonyms:
      self.union(wordA, wordB)
      
    # Create group map
    groupMap = defaultdict(list)
    for key in self.roots:
      root = self.find(key)
      groupMap[root].append(key)
      
    # Sort groups
    for key in groupMap:
      groupMap[key].sort()
    self.groupMap = groupMap
  
  def find(self, x):
    if x != self.roots[x]:
      self.roots[x] = self.find(self.roots[x])
    return self.roots[x]
  
  def union(self, x, y):
    xRoot, yRoot = self.find(x), self.find(y)
    self.roots[xRoot] = yRoot
  
  def exists(self, x):
    return x in self.roots
  
  def getGroup(self, x):
    return self.groupMap[self.find(x)]
  
  

class Solution:
  def generateSentences(self, synonyms, text):
    UF = UnionFind(synonyms)
      
    result = []
    textArr = text.split(' ')
    n = len(textArr)
    
    def DFS(index, path):
      if index == n:
        result.append(path.strip())
        return
      
      word = textArr[index]
      if UF.exists(word) == False:
        DFS(index + 1, path + ' ' + word)
      else:
        wordSynonyms = UF.getGroup(word)
        for syn in wordSynonyms:
          DFS(index + 1, path + ' ' + syn)
    
    DFS(0, '')
    return result
    
  
def runSolution():
  solution = Solution()
  print(solution.generateSentences(
    synonyms = [
      ["happy","joy"],
      ["sad","sorrow"],
      ["joy","cheerful"]], 
    text = "I am happy today but was sad yesterday"
  ))
  print(solution.generateSentences(
    synonyms = [
      ["happy","joy"],
      ["cheerful","glad"]], 
    text = "I am happy today but was sad yesterday"
  ))
  pass
runSolution()