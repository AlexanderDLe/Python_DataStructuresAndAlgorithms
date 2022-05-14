'''

  692. Top K Frequent Words

'''

from collections import Counter, deque
import heapq

class Node:
  def __init__(self, freq, word):
    self.freq = freq
    self.word = word
  
  def __lt__(self, other):
    if self.freq == other.freq: return self.word > other.word
    return self.freq < other.freq

class Solution:
  def topKFrequent(self, words, k):
    freqs = Counter(words)
    heap = []
    
    for item, freq in freqs.items():
      if len(heap) < k:
        heapq.heappush(heap, Node(freq, item))
      elif freq > heap[0].freq or (freq == heap[0].freq and item < heap[0].word):
        heapq.heappop(heap)
        heapq.heappush(heap, Node(freq, item))
        
    
    result = deque()
    while heap:
      result.appendleft(heapq.heappop(heap).word)
    
    return result
    
  

  
def runSolution():
  solution = Solution()
  print(solution.topKFrequent(words = ["i","love","leetcode","i","love","coding"], k = 2))
  print(solution.topKFrequent(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4))
  print(solution.topKFrequent(["i","love","leetcode","i","love","coding"], 3))
  pass
runSolution()