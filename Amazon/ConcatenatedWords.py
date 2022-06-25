'''

  472. Concatenated Words

'''


class Solution:
  def findAllConcatenatedWordsInADict(self, words):
    trie = self.buildTrie(words)
    result = []
    
    def DFS(word, index, count, memo):
      if index in memo: return
      if index == len(word) and count > 1: 
        result.append(word)
        return
      
      node = trie
      
      for i in range(index, len(word)):
        char = word[i]
        if char not in node: break
        
        node = node[char]
        if 'word' in node:
          DFS(word, i + 1, count + 1, memo)
          memo.add(i + 1)
    
    for word in words:
      DFS(word, 0, 0, set())
      
    return result
  
  def buildTrie(self, words):
    trie = {}
    for word in words:
      node = trie
      for char in word:
        node = node.setdefault(char, {})
      node['word'] = word
    return trie

def runSolution():
  solution = Solution()
  print(solution.findAllConcatenatedWordsInADict(
    words = ["cat","cats","catsdogcats","dog","dogcatsdog","hippopotamuses","rat","ratcatdogcat"]))
  print(solution.findAllConcatenatedWordsInADict(
    words = ["cat","dog","catdog"]))
  pass
runSolution()
