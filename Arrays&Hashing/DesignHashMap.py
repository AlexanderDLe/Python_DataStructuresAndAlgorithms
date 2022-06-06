'''

  706. Design HashMap

'''

class MyHashMap:
  def __init__(self):
    self.arr = [[] for _ in range(100)]

  def hash(self, key):
    return key % 100

  def put(self, key, value):
    hash = self.hash(key)
    for i, (k, _) in enumerate(self.arr[hash]):
      if k == key: 
        self.arr[hash][i][1] = value
        return
    self.arr[hash].append([key, value])

  def get(self, key):
    hash = self.hash(key)
    for (k, v) in self.arr[hash]:
      if k == key: return v
    return -1

  def remove(self, key):
    hash = self.hash(key)
    for i, (k, v) in enumerate(self.arr[hash]):
      if k == key:
        self.arr[hash].pop(i)
        return
      
  def print(self):
    print(self.arr)

def runSolution():
  myHashMap = MyHashMap()
  print(myHashMap.put(1, 1)) # The map is now [[1,1]]
  print(myHashMap.put(2, 2)) # The map is now [[1,1], [2,2]]
  print(myHashMap.get(1))    # return 1, The map is now [[1,1], [2,2]]
  print(myHashMap.get(3))    # return -1 (i.e., not found), The map is now [[1,1], [2,2]]
  print(myHashMap.put(2, 1)) # The map is now [[1,1], [2,1]] (i.e., update the existing value)
  print(myHashMap.get(2))    # return 1, The map is now [[1,1], [2,1]]
  print(myHashMap.remove(2)) # remove the mapping for 2, The map is now [[1,1]]
  print(myHashMap.get(2))    # return -1 (i.e., not found), The map is now [[1,1]]
  myHashMap.print()
  pass
runSolution()
