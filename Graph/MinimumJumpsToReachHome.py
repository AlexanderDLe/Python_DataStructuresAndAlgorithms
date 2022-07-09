'''

  1654. Minimum Jumps to Reach Home

'''

from collections import deque


class Solution:
  def minimumJumps(self, forbidden, a, b, x):
    self.visited = set([(0, False)])
    self.furthest = max(x, max(forbidden)) + a + b
    queue = deque([(0, False)])
    jumps = 0
    
    for pos in forbidden:
      self.visited.add((pos, True))
      self.visited.add((pos, False))
    
    while queue:
      for _ in range(len(queue)):
        pos, jumpedBack = queue.popleft()
        if pos == x: return jumps
        
        forward  = (pos + a, False)
        backward = (pos - b, True)
        
        if self.valid(forward):
          queue.append(forward)
          self.visited.add(forward)
          
        if self.valid(backward) and not jumpedBack:
          queue.append(backward)
          self.visited.add(backward)
        
      jumps += 1
    
    return -1
  
  def valid(self, move):
    if move in self.visited: return False
    if move[0] < 0: return False
    if move[0] > self.furthest: return False
    return True
    
  
def runSolution():
  solution = Solution()
  print(solution.minimumJumps(forbidden = [14,4,18,1,15], a = 3, b = 15, x = 9))
  print(solution.minimumJumps(forbidden = [8,3,16,6,12,20], a = 15, b = 13, x = 11))
  print(solution.minimumJumps(forbidden = [1,6,2,14,5,17,4], a = 16, b = 9, x = 7))
  print(solution.minimumJumps(
    [162,118,178,152,167,100,40,74,199,186,26,73,200,127,30,124,193,84,184,36,103,149,153,9,54,154,133,95,45,198,79,157,64,122,59,71,48,177,82,35,14,176,16,108,111,6,168,31,134,164,136,72,98],
    29,
    98,
    80
  ))
  pass
runSolution()