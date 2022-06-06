'''

  881. Boats to Save People

'''


from collections import deque


class Solution:
  def numRescueBoats(self, people, limit):
    people.sort()
    L, R = 0, len(people) - 1
    
    while R >= 0 and people[R] > limit:
      R -= 1
      
    count = 0
    
    while L <= R:
      capacity = 0
      
      capacity += people[R]
      R -= 1
      
      if L <= R and people[L] + capacity <= limit:
        capacity += people[L]
        L += 1
        
      count += 1
    
    return count
  

def runSolution():
  solution = Solution()
  print(solution.numRescueBoats(people = [1,2], limit = 3))
  print(solution.numRescueBoats(people = [3,2,2,1], limit = 3))
  print(solution.numRescueBoats(people = [3,5,3,4], limit = 5))
  print(solution.numRescueBoats([2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10], 50))
  pass
runSolution()