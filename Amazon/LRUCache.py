'''

  146. LRU Cache

  This implementation:
  
  Most recent       Next eviction    
  v                      v
  |----------------------|
  head                   tail

'''


class DoublyLinkedList:
  def __init__(self, key, val):
    self.key = key
    self.val = val
    self.prev = None
    self.next = None
    
  def detach(self):
    self.prev = None
    self.next = None
    

class LRUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.head = DoublyLinkedList(0, 0)
    self.tail = DoublyLinkedList(0, 0)
    self.head.next = self.tail
    self.tail.prev = self.head
    self.nodeMap = {}
    self.count = 0

  def get(self, key):
    if key not in self.nodeMap: return -1
    
    node = self.nodeMap[key]
    self.pluck(node)
    self.push(node)
    return node.val

  def put(self, key, value):
    # Key already exists in cache
    if key in self.nodeMap:
      node = self.nodeMap[key]
      self.pluck(node)
      self.push(node)
      node.val = value
      return
    
    # Key does not exist
    node = DoublyLinkedList(key, value)
    self.nodeMap[key] = node
    self.push(node)
    
    if self.count == self.capacity:
      poppedNode = self.pop()
      del self.nodeMap[poppedNode.key]
    else:
      self.count += 1
  
  def push(self, node):
    head = self.head
    prevHeadNext = head.next
    
    head.next = node
    node.prev = head
    node.next = prevHeadNext
    prevHeadNext.prev = node
    
  
  def pluck(self, node):
    nextNode = node.next
    prevNode = node.prev
    
    nextNode.prev = prevNode
    prevNode.next = nextNode
    node.detach()
  
  def pop(self):
    poppedNode = self.tail.prev
    self.pluck(poppedNode)
    return poppedNode
    
      
def runSolution():
  # lRUCache = LRUCache(2)
  # lRUCache.put(1, 1) # cache is {1=1}
  # lRUCache.put(2, 2) # cache is {1=1, 2=2}
  # print(lRUCache.get(1))    # return 1
  # lRUCache.put(3, 3) # LRU key was 2, evicts key 2, cache is {1=1, 3=3}
  # print(lRUCache.get(2))    # returns -1 (not found)
  # lRUCache.put(4, 4) # LRU key was 1, evicts key 1, cache is {4=4, 3=3}
  # print(lRUCache.get(1))    # return -1 (not found)
  # print(lRUCache.get(3))    # return 3
  # print(lRUCache.get(4))    # return 4
  
  lRUCache = LRUCache(2)
  lRUCache.put(2, 1)
  lRUCache.put(1, 1)
  lRUCache.put(2, 3)
  lRUCache.put(4, 1)
  print(lRUCache.get(1))   
  print(lRUCache.get(2))   
  
  ["LRUCache","put","put","put","put","get","get"]
  [[2],[2,1],[1,1],[2,3],[4,1],[1],[2]]
  pass
runSolution()