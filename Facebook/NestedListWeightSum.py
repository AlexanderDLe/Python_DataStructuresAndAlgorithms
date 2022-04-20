'''

  339. Nested List Weight Sum

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
  

def depthSum(nestedList):
  def processList(nList, level):
    total = 0
    for item in nList:
      if item.isInteger():
        total += (level * item.getInteger())
      else:
        total += processList(item.getList(), level + 1)

    return total

  
  return processList(nestedList, 1)



n3 = NestedInteger()
n3.add(NestedInteger(6))

n2 = NestedInteger()
n2.add(NestedInteger(4))
n2.add(n3)

n1 = NestedInteger()
n1.add(NestedInteger(1))

print(depthSum([n1, n2]))