'''

  843. Guess the Word

'''


from collections import deque
import random


class Solution:
  def findSecretWord(self, wordList, master):
    count = matches = 0
    
    while count < 10 and matches != 6:
      index = random.randint(0,len(wordList)-1)
      curr = wordList[index]
      matches = master.guess(curr)
      temp = []
      
      for word in wordList:
        if self.getMatchCount(curr, word) == matches: 
          temp.append(word)
      
      count += 1
      wordList = temp
        
  def getMatchCount(self, a, b):
    matches = 0
    for a, b in zip(a, b):
      if a == b: matches += 1
    return matches
  

def runSolution():
  solution = Solution()
  print(solution.findSecretWord(wordlist = ["acckzz","ccbazz","eiowzz","abcczz"]))
  print(solution.findSecretWord(wordlist = ["hamada","khaled"]))
  pass
runSolution()