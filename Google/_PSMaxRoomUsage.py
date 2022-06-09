'''
  
  Given 3 input parameters:   
  numRooms: Int, appointmentStartTimes: List[Int], appointmentDurations: List[Int]

  Return the usage number of the room that held the maximum appointments.

  Notes:

  appointmentStartTimes array is sorted
  the rooms should be assigned in the order. Meaning if room #2 and #3 are vacant, 
  we cannot execute next appointment in room 3, it has to be room #2.
  
  Example:

  numRooms: 3
  startTimes: [1, 3, 8, 13, 20]
  durations: [20, 3, 6, 2, 1]

  Expected output: 3
  Explanation:

  Room 1 is busy for the whole duration. So it is noticable that room 2 would be 
  the next go to for the following appointments.
  
  Appoitment at idx 1, 3, 4 would be held in room 2.
  
  1       3        8        13         20
  |--------------------------------------|
  1111111111111111111111111111111111111111
          222222   2222222222222        22
                             333333
'''

from collections import Counter
from heapq import heappush, heappop
from itertools import product


class Solution:
  def main(self, startTimes, durations):
    availableRooms, currentMeetings = [], []
    freqMap = Counter()
    mostFreq = 0
    roomNum = 1
    
    for start, duration in zip(startTimes, durations):
      while currentMeetings and currentMeetings[0][0] <= start:
        _, room = heappop(currentMeetings)
        heappush(availableRooms, room)
        
      if len(availableRooms) == 0:
        heappush(availableRooms, roomNum)
        roomNum += 1
        
      availRoom = heappop(availableRooms)
      freqMap[availRoom] += 1
      mostFreq = max(mostFreq, freqMap[availRoom])
      
      heappush(currentMeetings, (start + duration, availRoom))
    
    
    return mostFreq

  
def runSolution():
  solution = Solution()
  print(solution.main([1,3,8,13,20], [20,3,6,2,1]))
  pass
runSolution()