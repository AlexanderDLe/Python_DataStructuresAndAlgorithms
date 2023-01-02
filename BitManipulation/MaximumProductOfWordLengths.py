'''

  318. Maximum Product of Word Lengths

'''


from collections import defaultdict


class Solution:
  def maxProduct(self, words):
    binMap = defaultdict(int)
    ans = 0

    for word in words:
      for letter in word:
        binMap[word] |= 1 << (ord(letter) - 97)
    
    for i in range(len(words) - 1):
      for j in range(1, len(words)):
        word1, word2 = words[i], words[j]
        
        if binMap[word1] & binMap[word2] == 0:
          ans = max(ans, len(word1) * len(word2))
    
    return ans
    
  
def runSolution():
  solution = Solution()
  print(solution.maxProduct(words = ["abcw","baz","foo","bar","xtfn","abcdef"]))
  print(solution.maxProduct(words = ["a","ab","abc","d","cd","bcd","abcd"]))
  print(solution.maxProduct(words = ["a","aa","aaa","aaaa"]))
  pass
runSolution()
