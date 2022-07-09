'''

  792. Number of Matching Subsequences

'''

from collections import defaultdict


class SolutionTooSlow:
  def numMatchingSubseq(self, s, words):
    n = len(s)
    trie = self.buildTrie(words)
    count = 0
    
    def DFS(index, node):
      if 'word' in node:
        nonlocal count
        count += node['word']
        del node['word']
        
      if index == n: return
      
      char = s[index]
      
      if char in node:
        DFS(index + 1, node[char])
      DFS(index + 1, node)
    
    DFS(0, trie)
    return count
  
  def buildTrie(self, words):
    trie = {}
    for word in words:
      node = trie
      for char in word:
        node = node.setdefault(char, {})
        
      if 'word' in node: node['word'] += 1
      else: node['word'] = 1
    return trie

class SolutionRef:
  def numMatchingSubseq(self, s, words):
    wordDict = defaultdict(list)
    count = 0
    
    for word in words:
      wordDict[word[0]].append(word)
      
    for char in s:
      wordsExpectingChar = wordDict[char]
      wordDict[char] = []

      for word in wordsExpectingChar:
        if len(word) == 1:
          # Finished subsequence
          count += 1
        else:
          wordDict[word[1]].append(word[1:])
    
    return count
  
class Solution:
  def numMatchingSubseq(self, s, words):
    wordDict = defaultdict(list)
    
    for word in words:
      wordDict[word[0]].append(word)
      
    count = 0
    
    for char in s:
      candidates = wordDict[char]
      wordDict[char] = []
      
      for cand in candidates:
        if len(cand) == 1:
          count += 1
        else:
          wordDict[cand[1]].append(cand[1:])
          
    return count



def runSolution():
  solution = Solution()
  print(solution.numMatchingSubseq(
    s = "abcde", words = ["a","bb","acd","ace"]))
  print(solution.numMatchingSubseq(
    s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]))
  print(solution.numMatchingSubseq(
    "qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]))
  pass
runSolution()

