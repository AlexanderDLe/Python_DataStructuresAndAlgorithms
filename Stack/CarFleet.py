'''

  739. Daily Temperatures

  -------------------------------------------------
  
  Target = 12
  
  [pos, speed]
  [10, 2]
  [8, 4]
  [0, 1]
  [5, 1]
  [3, 3]
  
  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
     [10,2] [8,4]       [5,1]    [3,3]        [0,1] 
  |----------------------------------------------|
  12                                             0
  
  1. Sort by position
  
  [ [10,2], [8,4], [5,1], [3,3], [0,1] ]
  
  2. Utilize stack to combine fleets
  
  Stack
  Take [10, 2] and [8,4]
  
  2 mph.
  12 - 10 = 2 miles left until target.
  2miles left @ 2mph means it will take 1 hour to get there.
  
  [10, 2, 1]
          ^----- Hour(s) it will take to reach target.
          
  Take [8,4]
  4mph.
  12 - 8 = 4 miles left until target.
  4 miles left @ 4mph means it will take 1 hour to get there.
  
  [8, 4, 1]
  
  ---------------------
  
  [8,  4, 1]    <--- Looking at the time, we can see that 8 will catch up to 10
                     by the time they reach the destination. Therefore we can merge
                     with the slower one.
  [10, 2, 1]
                     
  ---------------------
  Next.
  
  Take [5, 1]
  12 - 5 = 7 miles left.
  7 miles left @ 1mph = 7 hours until it reaches destination.
  
  
  [5,  1, 7]    <---- Looking at the time, this will not catch up.
  [10, 2, 1]
  
  ---------------------
  
  Take [3, 3]
  12 - 3 = 9 miles left.
  9 miles left @ 3mph = 3 hours until it reaches destination.
  
  
  [3,  3, 3]    <---- Looking at the time, this will catch up the fleet
  [5,  1, 7]          that will take 7 hours to get there. So merge with slower.
  [10, 2, 1]
  
  ---------------------
  
  Take [0, 1]
  12 - 0 = 12 miles left.
  12 miles left @ 1mph = 12 hours until it reaches destination.
  
  It will not catch up to next fleet, therefore we can push onto stack.
  
  [0,  1, 12]
  [5,  1,  7]
  [10, 2,  1]
  
  _____
  
  Answer = 3 fleets.
'''

from functools import cmp_to_key


class SolutionMySolution:
  def carFleet(self, target, position, speed):
    n = len(speed)
    
    fleets = []
    for i in range(n):
      currPos, currSpeed = position[i], speed[i]
      distanceLeft = target - currPos
      timeUntilTarget = distanceLeft / currSpeed
      
      fleets.append((currPos, currSpeed, timeUntilTarget))
    
    fleets.sort(key=cmp_to_key(lambda a, b: b[0] - a[0]))
    stack = []
    print(fleets)
    for fleet in fleets:
      if not stack: 
        stack.append(fleet)
      else:
        top = stack[-1]
        if fleet[2] <= top[2]: continue
        else: stack.append(fleet)
    
    print(stack)
    return len(stack)
  
class Solution1:
  def carFleet(self, target, position, speed):
    pair = [[p, s] for p, s in zip(position, speed)]
    stack = []
    
    for p, s in sorted(pair)[::-1]:
      stack.append((target - p) / s)
      if len(stack) >= 2 and stack[-1] <= stack[-2]:
        stack.pop()
    
    return len(stack)

'''
  4 miles left @ 2mph = 2 hours until target
  15 miles left @ 5mph = 3 hours until target
'''

class Solution:
  def carFleet(self, target, position, speed):
    pairs = [(pos, spd) for pos, spd in zip(position, speed)]
    pairs.sort(reverse = True)
    stack = []
    
    for pos, spd in pairs:
      milesToTarget = target - pos
      hoursUntilTarget = milesToTarget / spd
      
      if not stack or hoursUntilTarget > stack[-1]:
        stack.append(hoursUntilTarget)
    
    return len(stack)
      
     
    
  
def runSolution():
  solution = Solution()
  print(solution.carFleet(10, [0,4,2], [2,1,3]))
  # print(solution.carFleet(target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]))
  # print(solution.carFleet(target = 10, position = [3], speed = [3]))
  # print(solution.carFleet(target = 100, position = [0,2,4], speed = [4,2,1]))
  pass
runSolution()
