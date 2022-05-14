'''

  1048. Longest String Chain

'''

from collections import defaultdict, deque

class SolutionRef:
  def longestStrChain(self, words):
    words.sort(key=len)  # sort words by its length
    result = 0
    DP = defaultdict(int)
    print(words)
    
    for word in words:
      DP[word] = 1
      print('--word:', word)
      for i in range(len(word)):
        predecessor = word[:i] + word[i+1:]
        print('pred:', predecessor)
        if predecessor in DP and DP[word] < DP[predecessor] + 1:
          print('match: ', predecessor)
          DP[word] = DP[predecessor] + 1
      print(DP)
            
      result = max(result, DP[word])
    
    print(DP)
    return result
      
  
      
class Solution:
  def longestStrChain(self, words):
    words.sort(key=len)
    result = 0
    DP = defaultdict(int)
    
    for word in words:
      DP[word] = 1
      
      for i in range(len(word)):
        substr = word[:i] + word[i + 1:]
        
        if substr in DP:
          DP[word] = max(DP[word], DP[substr] + 1)
      
      result = max(result, DP[word])
    
    return result
    
    
  
def runSolution():
  solution = Solution()
  print(solution.longestStrChain(words = ["a","b","ba","bca","bda","bdca"]))
  print(solution.longestStrChain(words = ["xbc","pcxbcf","xb","cxbc","pcxbc"]))
  print(solution.longestStrChain(words = ["abcd","dbqca"]))
  pass
runSolution()