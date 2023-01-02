'''

  347. Top K Frequent Elements

'''


from collections import Counter
import heapq
    
class SolutionHeap:
  class HeapNode:
    def __init__(self, value, freq):
      self.value = value
      self.freq = freq
    def __lt__(self, other):
      return self.freq < other.freq
    
  def topKFrequent(self, nums, k):
    freqDict = Counter()
    for num in nums:
      freqDict[num] += 1
      
    heap = []
    for num, freq in freqDict.items():
      if len(heap) < k:
        heapq.heappush(heap, self.HeapNode(num, freq))
      else:
        if freq <= heap[0].freq: continue
        heapq.heappop(heap)
        heapq.heappush(heap, self.HeapNode(num, freq))
      
    return list(map(lambda x: x.value, heap))

class SolutionBucketSort:
  def topKFrequent(self, nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    freqMap = Counter()
    
    for num in nums:
      freqMap[num] += 1
        
    for num, freq in freqMap.items():
      buckets[freq].append(num)
    
    # buckets is a double array
    flat_list = []
    # traverse from right to left so number with higher frequency come first
    for i in range(len(buckets) - 1, -1, -1):
      bucket = buckets[i]
      if bucket:
        for num in bucket:
          flat_list.append(num)
          
    print(buckets)
    print(flat_list)
    return flat_list[:k]

    
class Solution:
  
  '''
  
    Time Complexity
    O(n) To iterate through all numbers
    
    Space Complexity
    O(n) where n is the size of the input array to hold all buckets
  
  '''
  
  def topKFrequent(self, nums, k):
    buckets = [[] for _ in range(len(nums) + 1)]
    freqMap = Counter(nums)
    
    # Place items in buckets according to their frequency
    for num, freq in list(freqMap.items()):
      buckets[freq].append(num)
    
    # Iterate backwards from the end of the array, placing
    # items with greater frequency first until k is reached.
    result = []
    index = len(nums) - 1
    
    while index >= 0 and len(result) < k:
      bucket = buckets[index]
      
      if bucket: result.append(bucket.pop())
      else: index -= 1
    
    return result

    
  
def runSolution():
  solution = Solution()
  print(solution.topKFrequent(nums = [1,1,1,2,2,2,2,3], k = 2))
  # print(solution.topKFrequent(nums = [1], k = 1))
  pass
runSolution()
