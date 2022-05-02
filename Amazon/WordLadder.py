'''

  126. Word Ladder II

  "hot","dot","dog","lot","log","cog"
  
  hot = *ot, h*t, ho*
'''
from collections import defaultdict
from string import ascii_lowercase


class SolutionRef:
  def findLadders(self, beginWord, endWord, wordList):
    remainingWords = set(wordList)                       # to check if a word is existed in the wordSet, in O(1)
    remainingWords.discard(beginWord)

    def neighbors(word):
      for i in range(len(word)):                  # change every possible single letters and check if it's in wordSet
        for c in ascii_lowercase:
          newWord = word[:i] + c + word[i + 1:]
          if newWord in remainingWords:
            yield newWord

    level = {}
    level[beginWord] = [[beginWord]]              # level[word] is all possible sequence paths which start from beginWord and end at `word`.
    
    while level:
      nextLevel = defaultdict(list)
      
      print('remainingWords', remainingWords)
      print(level.items())
      for word, paths in level.items():
        if word == endWord:
          return paths                            # return all shortest sequence paths
        
        print(word)
        for nei in neighbors(word):
          print(nei)
          for path in paths:
            nextLevel[nei].append(path + [nei])   # form new paths with `nei` word at the end
            
      remainingWords -= set(nextLevel.keys())            # remove visited words to prevent loops
      level = nextLevel                           # move to new level

    return []
  
class Solution:
  def findLadders(self, beginWord, endWord, wordList):
    remainingWords = set(wordList)
    remainingWords.discard(beginWord)
    
    level = {beginWord: [[beginWord]]}
    
    while level:
      nextLevel = defaultdict(list)
      
      for word, paths in level.items():
        if word == endWord: return paths
        
        for neighbor in self.findNeighbors(remainingWords, word):
          for path in paths:
            nextLevel[neighbor].append(path + [neighbor])
      
      remainingWords -= set(level.keys())
      level = nextLevel
      
    return []    
  
  def findNeighbors(self, remainingWords, word):
    neighbors = []    
    for i in range(len(word)):
      for c in ascii_lowercase:
        newWord = word[:i] + c + word[i + 1:]
        if newWord in remainingWords: neighbors.append(newWord)
    
    return neighbors
    
    
  
def runSolution():
  solution = Solution()
  print(solution.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]))
  # print(solution.findLadders(beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]))
  pass
runSolution()