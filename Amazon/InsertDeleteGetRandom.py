'''

  380. Insert Delete GetRandom O(1)

'''

from operator import index
from random import randrange


class RandomizedSet:
  def __init__(self):
    self.dict = {}
    self.array = []

  def insert(self, val):
    if val in self.dict: return False
    self.dict[val] = len(self.array)
    self.array.append(val)
    return True

  def remove(self, val: int):
    if val not in self.dict: return False
    array = self.array
    
    # If val is last item, then pop and update dict
    if val == array[-1]:
      del self.dict[val]
      array.pop()
      return True
    
    # Swap last item and removed item in array
    indexToRemove = self.dict[val]
    lastVal = array.pop()
    array[indexToRemove] = lastVal
    
    # Index must be updated in dictionary
    self.dict[lastVal] = indexToRemove
    del self.dict[val]
    
    return True

  def getRandom(self):
    rand = randrange(0, len(self.array))
    return self.array[rand]
  
def runSolution():
  randomizedSet = RandomizedSet();
  print(randomizedSet.insert(1))    # Inserts 1 to the set. Returns true as 1 was inserted successfully.
  print(randomizedSet.remove(2))    # Returns false as 2 does not exist in the set.
  print(randomizedSet.insert(2))    # Inserts 2 to the set, returns true. Set now contains [1,2].
  print(randomizedSet.getRandom())  # getRandom should return either 1 or 2 randomly.
  print(randomizedSet.remove(1))    # Removes 1 from the set, returns true. Set now contains [2].
  print(randomizedSet.insert(2))    # 2 was already in the set, so return false.
  print(randomizedSet.getRandom())  # Since 2 is the only number in the set, getRandom() will always return 2.
runSolution()