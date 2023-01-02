'''

  242. Valid Anagram

'''


from collections import Counter


class Solution1:
  def isAnagram(self, s, t):
    sFreq, tFreq = self.buildFreq(s), self.buildFreq(t)
    return sFreq == tFreq
    
  def buildFreq(self, word):
    freqDict = Counter()
    for char in word:
      freqDict[char] += 1
    return freqDict

class Solution:
  def isAnagram(self, s, t):
    return Counter(s) == Counter(t)
  
  
  
def runSolution():
  solution = Solution()
  print(solution.isAnagram(s = "anagram", t = "nagaram"))
  print(solution.isAnagram(s = "rat", t = "car"))
  pass
runSolution()
