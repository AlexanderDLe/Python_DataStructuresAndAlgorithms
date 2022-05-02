'''

  387. First Unique Character in a String

'''

class Solution:
  def firstUniqChar(self, s):
    freqMap = {}
    for char in s: 
      freqMap[char] = freqMap.get(char, 0) + 1
      
    for i, char in enumerate(s):
      if freqMap[char] == 1: return i
    return -1
  
  
  
def runSolution():
  solution = Solution()
  print(solution.firstUniqChar('leetcode'))
  print(solution.firstUniqChar('loveleetcode'))
  print(solution.firstUniqChar('aabb'))
runSolution()