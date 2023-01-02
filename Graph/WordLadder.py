'''

  127. Word Ladder

'''

from collections import Counter, defaultdict, deque


class Solution:
  def ladderLength(self, beginWord, endWord, wordList):
    patternDict = self.buildPatterns(wordList)
    queue = deque([beginWord])
    seen  = set([beginWord])
    moves = 0
    
    while queue:
      moves += 1
      
      for _ in range(len(queue)):
        word = queue.popleft()
        if word == endWord: return moves
        
        for pattern in self.getPatterns(word):
          candidates = patternDict[pattern]
          
          for candidate in candidates:
            if candidate in seen: continue
            seen.add(candidate)
            queue.append(candidate)
    
    return 0
  
  
  def buildPatterns(self, wordList):
    patternDict = defaultdict(list)
    for word in wordList:
      for pattern in self.getPatterns(word):
        patternDict[pattern].append(word)
    return patternDict
  
  def getPatterns(self, word):
    patterns, n = [], len(word)
    for i in range(n):
      patterns.append(word[:i] + '*' + word[i + 1:])
    return patterns


  
def runSolution():
  solution = Solution()
  
  print(solution.ladderLength(
    beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
  print(solution.ladderLength(
    beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
  pass
runSolution()