'''

  841. Keys and Rooms

'''


from collections import deque


class Solution:
  def canVisitAllRooms(self, rooms):
    totalRooms = len(rooms)
    queue = deque([0])
    seen = set([0])
    
    while queue:
      curr = queue.popleft()
      
      for next in rooms[curr]:
        if next in seen: continue
        seen.add(next)
        queue.append(next)
    
    return len(seen) == totalRooms
    

    
    
  
def runSolution():
  solution = Solution()
  print(solution.canVisitAllRooms(rooms = [[1],[2],[3],[]]))
  print(solution.canVisitAllRooms(rooms = [[1,3],[3,0,1],[2],[0]]))
  pass
runSolution()