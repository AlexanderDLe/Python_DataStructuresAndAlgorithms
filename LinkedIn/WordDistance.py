'''

  244. Shortest Word Distance II
  
  Edge Cases:
  1. What if there are duplicate words?
  2. What if word doesn't exist?

'''

class WordDistance:
  def __init__(self, wordsDict):
    self.indexMap = {}
    
    for i, word in enumerate(wordsDict):
      self.indexMap[word] = self.indexMap.get(word, []) + [i]
      
    print(self.indexMap)
    
  def shortest(self, word1, word2):
    indexes1 = self.indexMap[word1]
    indexes2 = self.indexMap[word2]
    p1 = p2 = 0
    
    minDistance = float('inf')
    
    while p1 < len(indexes1) and p2 < len(indexes2):
      index1, index2 = indexes1[p1], indexes2[p2]
      minDistance = min(minDistance, abs(index1 - index2))
      
      if index1 < index2: p1 += 1
      else              : p2 += 1
    
    return minDistance


obj = WordDistance(["practice", "makes", "perfect", "coding", "makes", "practice"])
print(obj.shortest("coding","practice"))
print(obj.shortest("coding","makes"))