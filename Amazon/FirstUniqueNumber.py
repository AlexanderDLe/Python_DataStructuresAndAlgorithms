'''

  1429. First Unique Number

'''


from collections import defaultdict, deque


class FirstUnique:
  def __init__(self, nums):
    self.freqDict = defaultdict(int)
    self.queue = deque()
    
    for num in nums:
      self.add(num)

  def showFirstUnique(self):
    while self.queue:
      first = self.queue[0]
      if self.freqDict[first] > 1: self.queue.popleft()
      else: break
    
    return self.queue[0] if self.queue else -1

  def add(self, value):
    self.freqDict[value] += 1
    if self.freqDict[value] == 1: self.queue.append(value)


def runSolution():
  firstUnique = FirstUnique([2,3,5])
  print(firstUnique.showFirstUnique())   # return 2
  print(firstUnique.add(5))              # the queue is now [2,3,5,5]
  print(firstUnique.showFirstUnique())   # return 2
  print(firstUnique.add(2))              # the queue is now [2,3,5,5,2]
  print(firstUnique.showFirstUnique())   # return 3
  print(firstUnique.add(3))              # the queue is now [2,3,5,5,2,3]
  print(firstUnique.showFirstUnique())   # return -1
  
  firstUnique2 = FirstUnique([7,7,7,7,7,7]);
  print(firstUnique2.showFirstUnique())  # return -1
  print(firstUnique2.add(7))             # the queue is now [7,7,7,7,7,7,7]
  print(firstUnique2.add(3))             # the queue is now [7,7,7,7,7,7,7,3]
  print(firstUnique2.add(3))             # the queue is now [7,7,7,7,7,7,7,3,3]
  print(firstUnique2.add(7))             # the queue is now [7,7,7,7,7,7,7,3,3,7]
  print(firstUnique2.add(17))            # the queue is now [7,7,7,7,7,7,7,3,3,7,17]
  print(firstUnique2.showFirstUnique())  # return 17

runSolution()