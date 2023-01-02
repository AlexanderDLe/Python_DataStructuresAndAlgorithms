'''
  
  Given a set of words, find the longest chain of words that can be made out of those words with the following rules:

  Each word in the chain is one letter longer than the previous word.

  Each word in the chain differs from the previous word only by its last letter.

  Write test case's. Also, mention the Time and Space complexity for the same.

  Constraint Examples: 

  den -> dent-> dents is valid (meets all constraints) 

  den -> dew is not valid (same length: 3 characters) 

  den -> cent is not valid (differs by 1’st char [‘d’ != ‘c’]) 
  Example:

  Input: {ben, bent, dew, dents, dent, bet, den}

  Output: 3 ({den, dent, dents})
  
'''


from collections import defaultdict


class Solution:
  def main(self, words):
    words.sort(key = lambda x: len(x))
    lenMap = defaultdict(int)
    result = 0
    
    for word in words:
      lenMap[word] = 1
      prefix = word[0:len(word) - 1]
      
      if prefix in lenMap:
        lenMap[word] = max(lenMap[word], lenMap[prefix] + 1)
        result = max(result, lenMap[word])
    
    print(lenMap)
    return result
  
def runSolution():
  solution = Solution()
  print(solution.main(words = ['be', 'ben', 'bent', 'dew', 'dents', 'dent', 'bet', 'den']))
  pass
runSolution()