'''

  752. Open the Lock

'''


from collections import deque


class Solution:
  def openLock(self, deadends, target):
    deadends = set(deadends)
    if '0000' in deadends: return -1
    
    moves = 0
    seen = set(['0000'])
    queue = deque(['0000'])
    
    while queue:
      for _ in range(len(queue)):
        node = queue.popleft()
        
        if node in deadends: continue
        if node == target: return moves
        
        for i in range(4):
          inc = node[:i] + str((int(node[i]) + 1) % 10) + node[i + 1:]
          dec = node[:i] + str((int(node[i]) - 1) % 10) + node[i + 1:]
          if inc not in seen: 
            queue.append(inc)
            seen.add(inc)
          if dec not in seen: 
            queue.append(dec)
            seen.add(dec)
      
      moves += 1
    
    return -1
    
    
  
def runSolution():
  solution = Solution()
  print(solution.openLock(
    deadends = ["0201","0101","0102","1212","2002"], target = "0202"))
  print(solution.openLock(
    deadends = ["8888"], target = "0009"))
  print(solution.openLock(
    deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"))
  pass
runSolution()