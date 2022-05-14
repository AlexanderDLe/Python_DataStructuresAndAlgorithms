'''

  139. Word Break

'''

class Solution:
  def wordBreak(self, s, wordDict):
    n = len(s)
    trie = self.buildTrie(wordDict)
    self.result = False
    memo = set()
    
    def DFS(index, node):
      if index == n: self.result = True
      if index >= n or self.result or index in memo: return
      memo.add(index)
      
      for i in range(index, n):
        char = s[i]
        if char not in node: return
        
        node = node[char]
        if 'word' in node: DFS(i + 1, trie)
    
    DFS(0, trie)
    return self.result
  
  def buildTrie(self, wordDict):
    trie = {}
    for word in wordDict:
      node = trie
      for char in word:
        node = node.setdefault(char, {})
      node['word'] = True
    return trie



def runSolution():
  solution = Solution()
  print(solution.wordBreak(
    s = "leetcode", wordDict = ["leet","code"]))
  print(solution.wordBreak(
    s = "applepenapple", wordDict = ["apple","pen"]))
  print(solution.wordBreak(
    s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))
  pass
runSolution()

