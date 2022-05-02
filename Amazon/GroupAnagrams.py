'''

  49. Group Anagrams

'''

class Solution:
  def groupAnagrams(self, strs):
    wordDict = {}
    
    for str in strs:
      word = ''.join(sorted(list(str)))
      wordDict[word] = wordDict.get(word, []) + [str]
      
    return list(wordDict.values())
  
  
def runSolution():
  solution = Solution()
  print(solution.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
runSolution()