'''

  846. Hand of Straights
  
'''

from collections import Counter, defaultdict
import heapq


class SolutionFreqs:
  def isNStraightHand(self, hand, groupSize):
    n = len(hand)
    if n % groupSize: return False
    
    freqs = Counter(hand)
    count = 0
    
    # Itereate through entire hand
    while count < n:
      # start with available min val at start of every group
      start = min(freqs.keys())
      # check if incrementing group build is possible
      for i in range(groupSize):
        num = start + i
        if num not in freqs: return False
        
        freqs[num] -= 1
        if not freqs[num]: del freqs[num]
        
        i += 1
        count += 1
    
    return True

class Solution:
  def isNStraightHand(self, hand, groupSize):
    n = len(hand)
    
    if n % groupSize: return False
    
    freqs = Counter(hand)
    heapq.heapify(hand)
    
    for i in range(n // groupSize):
      start = heapq.heappop(hand)
      
      while freqs[start] == 0:
        start = heapq.heappop(hand)
      
      for i in range(groupSize):
        num = start + i
        if freqs[num] == 0: return False
        freqs[num] -= 1
    
    return True


def runSolution():
  solution = Solution()
  print(solution.isNStraightHand(hand = [1,2,3,6,2,3,4,7,8], groupSize = 3))
  print(solution.isNStraightHand(hand = [1,2,3,4,5], groupSize = 4))
  print(solution.isNStraightHand(
    [9,13,15,23,22,25,4,4,29,15,8,23,12,19,24,17,18,11,22,24,17,17,10,23,21,18,14,18,
     7,6,3,6,19,11,16,11,12,13,8,26,17,20,13,19,22,21,27,9,20,15,20,27,8,13,25,23,22,
     15,9,14,20,10,6,5,14,12,7,16,21,18,21,24,23,10,21,16,18,16,18,5,20,19,20,10,14,
     26,2,9,19,12,28,17,5,7,25,22,16,17,21,11],10))
  pass
runSolution()
