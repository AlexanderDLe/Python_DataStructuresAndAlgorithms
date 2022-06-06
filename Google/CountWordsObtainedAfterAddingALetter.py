'''

  2135. Count Words Obtained After Adding a Letter

  Example:
  startWords = ["ant","act","tack"], 
  targetWords = ["tack","act","acti"]
  
  ------------------------------------------------------------------
  
  To reach target, requirement is you must append one word. Therefore, 
  targetWords must be sourced from startWords that have one less char.
  
  To simplify, we can use a lenMap to order startWords:
  
  startWords = ["ant","act","tack"]
  
  lenMap = {
    3: ['ant', 'act']
    4: ['tack']
  }
  
  ------------------------------------------------------------------
  
  Now for every target word, we can search through the startWords that have -1 len.
  
  Ex. targetWord = 'tack' with len of 4
  
  Search through len of 3 in lenMap:
  ['ant', 'act']
  
  To build any of these startWords into the targetWord, targetWord must contain all words of startWord.
  Ex: 'tack' contains all of 'act', therefore it can be built by appending & rearranging.
  
  'act' -> add 'k' -> rerrange into 'tack'
  
  ------------------------------------------------------------------
  
  How can we efficiently determine if tack can be built from start words?
  
  target = 'tack'
  start  = ['ant', 'act']
  
  alphabetize? 
  target = 'tack' -> 'ackt'
  start  = ['ant', 'act', tck']
  
  Make a trie for every len?
          a       c
        c    n    k
        t    t    t
          
  For every targetWord, we can try to traverse its corresponding len-1 trie
  and try to reach the end.
  
  If we encounter a letter in targetWord that does not exist, we can use a wildcard.
'''

from collections import defaultdict

class Solution:
  def wordCount(self, startWords, targetWords):
    def wordBinary(word):
      ans = ['0'] * 26
      for c in word:
        ans[ord(c) - ord('a')] = '1'
      return ''.join(ans)
  
    startSet = set()
    for word in startWords:
      startSet.add(wordBinary(word))
      
    res = 0
    
    for word in targetWords:
      for i in range(len(word)):
        candidate = word[:i] + word[i + 1:]
        if wordBinary(candidate) in startSet:
          res += 1
          break
    
    return res
  
  
  
  
def runSolution():
  solution = Solution()
  print(solution.wordCount(
    startWords = ["ant","act","tack"], 
    targetWords = ["tack","act","acti"]))
  print(solution.wordCount(
    startWords = ["ab","a"], 
    targetWords = ["abc","abcd"]))
  pass
runSolution()