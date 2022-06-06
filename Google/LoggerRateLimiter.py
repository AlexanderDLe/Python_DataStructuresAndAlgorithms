'''

  2158. Amount of New Area Painted Each Day

'''


from collections import defaultdict, deque
import heapq


class Logger:
  def __init__(self):
    self.timestampMap = defaultdict(lambda: float('-inf'))

  def shouldPrintMessage(self, timestamp, message):
    if timestamp - self.timestampMap[message] >= 10:
      self.timestampMap[message] = timestamp
      return True
    
    return False
      
        
def runSolution():
  logger = Logger()
  print(logger.shouldPrintMessage(1, "foo"))  # return true, next allowed timestamp for "foo" is 1 + 10 = 11
  print(logger.shouldPrintMessage(2, "bar"))  # return true, next allowed timestamp for "bar" is 2 + 10 = 12
  print(logger.shouldPrintMessage(3, "foo"))  # 3 < 11, return false
  print(logger.shouldPrintMessage(8, "bar"))  # 8 < 12, return false
  print(logger.shouldPrintMessage(10, "foo")) # 10 < 11, return false
  print(logger.shouldPrintMessage(11, "foo")) # 11 >= 11, return true, next allowed timestamp for "foo" is 11 + 10 = 21
  pass
runSolution()