'''

  646. Maximum Length of Pair Chain

  [1,2],[2,3],[3,4]

   a b                   c d
  [1,2] does not follow [2,3] because 2 not < 2
  
  Step 1. Sort the pairs
  
'''

class Solution:
  def findLongestChain(self, pairs):
    if len(pairs) < 2: return len(pairs)
    
    n = len(pairs)
    pairs.sort(reverse = True)
    arr = [[1, pair] for pair in pairs]
    maxLen = 0
    
    for i in range(1, n):
      for j in range(i-1, -1, -1):
        _______, currPair = arr[i]
        prevLen, prevPair = arr[j]
        
        if self.canFollow(currPair, prevPair):
          arr[i][0] = max(arr[i][0], prevLen + 1)
        
        maxLen = max(maxLen, arr[i][0])
  
    return maxLen
  
  def canFollow(self, currPair, prevPair):
    return currPair[1] < prevPair[0]
  
  
  
class Solution:
  def findLongestChain(self, pairs):
    maxLen = 0
    pairs.sort(key=lambda x: x[1])
    curr = float('-inf')
    
    for head, tail in pairs:
      if head > curr:
        maxLen += 1
        curr = tail
  
    return maxLen
  
  

def runSolution():
  solution = Solution()
  print(solution.findLongestChain(pairs = [[1,2],[2,3],[3,4]]))
  print(solution.findLongestChain(pairs = [[1,2],[7,8],[4,5]]))
  print(solution.findLongestChain(pairs = [[1,2]]))
  print(solution.findLongestChain(pairs = []))
  pass
runSolution()