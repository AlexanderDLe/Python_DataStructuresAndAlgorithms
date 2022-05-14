'''

  1584. Min Cost to Connect All Points

'''

from collections import Counter, defaultdict, deque

class Solution:
  def alienOrder(self, words):
    inDegrees, parents, queue, charCount, valid = self.init(words)
    seen = set()
    result = ''
    
    if not valid: return ''
    
    while queue:
      letter = queue.popleft()
      if letter in seen: return ''
      
      seen.add(letter)
      result += letter
      
      for child in parents[letter]:
        inDegrees[child] -= 1
        if not inDegrees[child]: queue.append(child)
    
    return result if charCount == len(result) else 0
  

  def init(self, words):
    inDegrees, parents, sourceSet = Counter(), defaultdict(list), set()
    valid = True
    
    for word in words:
      for char in word:
        sourceSet.add(char)
    
    charCount = len(sourceSet)
    
    for i in range(len(words) - 1):
      curr, next = words[i], words[i + 1]
      c = n = 0
      
      if self.invalidPrefix(curr, next): 
        valid = False
        break
      
      while c < len(curr) and n < len(next) and curr[c] == next[n]:
        c += 1
        n += 1
      
      if c >= len(curr) or n >= len(next): continue
      
      sourceSet.discard(next[n])
      inDegrees[next[n]] += 1
      parents[curr[c]].append(next[n])
    
    return inDegrees, parents, deque(list(sourceSet)), charCount, valid

  def invalidPrefix(self, curr, next):
    if len(curr) > len(next) and curr[0: len(next)] == next: return True
    return False
    

  
def runSolution():
  solution = Solution()
  print(solution.alienOrder(["ac","ab","b"]))
  # print(solution.alienOrder(["wrt","wrf","er","ett","rftt"]))
  # print(solution.alienOrder(["z","x"]))
  # print(solution.alienOrder(["z","x","z"]))
  # print(solution.alienOrder(["z","z"]))
  pass
runSolution()