'''

  460. LFU Cache

  LRU Cache With Frequency Map?
  
  head                tail
  |----------------------|
  ^                      ^
  Most Recent            Least Recent
  
  LFU aspect: 
  Least frequent element is removed. If there is a tie,
  then use LRU mechanism.
  
  How to keep track of frequency? Min Heap with lazy delete?
  When an item is modified, then add (freq, node) to minHeap.
  
  
  LRU aspect: move DLL node when node is accessed/placed.
  
'''

from collections import defaultdict

class DoubleNode:
  def __init__(self):
    pass

class LRUList:
  def __init(self):
    pass

class LFUCache:
  def __init__(self, capacity):
    self.capacity = capacity
    self.LFUMap = defaultdict(list)

  def get(self, key):
    pass

  def put(self, key, value):
    pass
    
        

def runSolution():
  lfu = LFUCache(2)
  lfu.put(1, 1)   # cache=[1,_], cnt(1)=1
  lfu.put(2, 2)   # cache=[2,1], cnt(2)=1, cnt(1)=1
  lfu.get(1)      # return 1
                  # cache=[1,2], cnt(2)=1, cnt(1)=2
  lfu.put(3, 3)   # 2 is the LFU key because cnt(2)=1 is the smallest, invalidate 2.
                  # cache=[3,1], cnt(3)=1, cnt(1)=2
  lfu.get(2)      # return -1 (not found)
  lfu.get(3)      # return 3
                  # cache=[3,1], cnt(3)=2, cnt(1)=2
  lfu.put(4, 4)   # Both 1 and 3 have the same cnt, but 1 is LRU, invalidate 1.
                  # cache=[4,3], cnt(4)=1, cnt(3)=2
  lfu.get(1)      # return -1 (not found)
  lfu.get(3)      # return 3
                  # cache=[3,4], cnt(4)=1, cnt(3)=3
  lfu.get(4)      # return 4
                  # cache=[4,3], cnt(4)=2, cnt(3)=3
  pass
runSolution()

