'''

  398. Random Pick Index

'''

from random import randrange


class Solution:
  def __init__(self, nums):
    self.dict = {}

    for i, num in enumerate(nums):
      if num not in self.dict: self.dict[num] = []
      self.dict[num].append(i)

  def pick(self, target):
    indexes = self.dict[target]
    rand = randrange(0, len(indexes))
    return indexes[rand]
    


solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))
print(solution.pick(1))
print(solution.pick(3))