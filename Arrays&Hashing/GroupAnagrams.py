'''

  49. Group Anagrams

'''


from collections import defaultdict


class Solution:
  def groupAnagrams(self, strs):
    dict = defaultdict(list)
    
    for str in strs:
      dict[''.join(sorted(str))].append(str)
      
    return dict.values()
  
def runSolution():
  solution = Solution()
  print(solution.groupAnagrams(strs = ["eat","tea","tan","ate","nat","bat"]))
  pass
runSolution()
