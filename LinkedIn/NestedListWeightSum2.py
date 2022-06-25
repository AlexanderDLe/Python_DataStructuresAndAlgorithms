'''

  364. Nested List Weight Sum II

  The weight of an integer is maxDepth - (the depth of the integer) + 1.
  Return the sum of each integer in nestedList multiplied by its weight.
'''

class NestedInteger:
  def __init__(self, value=None):
    self.value = value
    self.nestedList = []

  def __repr__(self):
    return f'(value: {self.value} | list: {self.nestedList})'

  def isInteger(self):
    return self.value != None
  
  def getInteger(self):
    return self.value if self.value != None else None  

  def setInteger(self, value):
    self.value = value  

  def add(self, elem):
    self.nestedList.append(elem)  

  def getList(self):
    return self.nestedList if len(self.nestedList) > 0 else None
  
def depthSumInverse(nestedInteger):
  maxDepth = 0
  
  def getMaxDepth(nestedInt, depth):
    nonlocal maxDepth
    maxDepth = max(maxDepth, depth)
    
    for item in nestedInt:
      if item.isInteger(): continue
      else: getMaxDepth(item.getList(), depth + 1)
    
  def process(nestedInt, depth):
    total = 0
    weight = maxDepth - depth + 1
    
    for item in nestedInt:
      if item.isInteger():
        total += (item.getInteger() * weight)
      else:
        total += process(item.getList(), depth + 1)
    return total
    
  getMaxDepth(nestedInteger, 1)
  return process(nestedInteger, 1)
  


n3 = NestedInteger()
n3.add(NestedInteger(6))

n2 = NestedInteger()
n2.add(NestedInteger(4))
n2.add(n3)

n1 = NestedInteger(1)
# n1.add(NestedInteger(1))

print(depthSumInverse([n1, n2]))