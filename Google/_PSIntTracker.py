'''

  Problem

  Tracker - it tracks integers
  - track(int) -> Keeps track of the given integer
  - min() -> Returns the smallest integer tracked so far
  - max() -> largest
  - mean() -> avg
  - mode() -> Returns the integer that has been tracked the most
  All of these methods must be O(1) - constant time


  _____________________________________________________________________________

  Example:

  track(1)
  track(2)
  track(1)
  track(8)

  min = 1
  max = 8
  mean = (1 + 2 + 1 + 8)/4 = 12/4 = 3
  mode = 1

  _____________________________________________________________________________

  Constraints

  1. All points are unique
  2. All points are valid x and y coordinates
  3. Max points is 50

  _____________________________________________________________________________


  Strategy

  Maintain relevant variables

  _____________________________________________________________________________


'''

from collections import Counter


class Solution:
  def __init__(self):
    self.minVal = float('inf')
    self.maxVal = float('-inf')
    self.sum = 0
    self.ints = 0
    self.freqMap = Counter()
    self.mostFreq = 0
    self.modeVal = 0

  def track(self, int):
    self.minVal = min(self.minVal, int)
    self.maxVal = max(self.maxVal, int)
    self.sum += int
    self.ints += 1

    self.freqMap[int] += 1
    if self.freqMap[int] > self.mostFreq:
      self.mostFreq = self.freqMap[int]
      self.modeVal = int
      
    print(self.freqMap)

  def min(self):
    return self.minVal

  def max(self):
    return self.maxVal

  def mean(self):
    return self.sum/self.ints

  def mode(self):
    return self.modeVal

  
def runSolution():
  solution = Solution()
  solution.track(1)
  solution.track(2)
  solution.track(1)
  solution.track(8)
  print(solution.min())
  print(solution.max())
  print(solution.mean())
  print(solution.mode())
  pass
runSolution()