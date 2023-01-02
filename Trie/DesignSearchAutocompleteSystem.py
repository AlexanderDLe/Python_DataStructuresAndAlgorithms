'''

  642. Design Search Autocomplete System

'''

from bisect import insort_left
from collections import defaultdict


class AutocompleteSystem:
  def __init__(self, sentences, times):
    self.trie = {}
    
    for sentence, time in zip(sentences, times):
      self.storeInput(sentence, time)
    
    self.currNode = self.trie
    self.currInput = ''
  
  def storeInput(self, input, time):
    node = self.trie
    for char in input:
      node = node.setdefault(char, {})
    
    if 'word' in node:
      prevTime, input = node['word']
      node['word'] = (prevTime + 1, input)
    else:
      node['word'] = (time, input)
  
  def input(self, char: str):
    if char == '#':
      self.storeInput(self.currInput, 1)
      self.currInput = ''
      self.currNode = self.trie
      return []
    
    self.currInput += char
    
    if char not in self.currNode:
      self.currNode = {}
      return []
    
    self.currNode = self.currNode[char]
    
    candidates = defaultdict(list)
    self.DFS(self.currNode, candidates)
    candidates = list(candidates.items())
    candidates.sort(reverse = True)
    result = []
    
    for cand in candidates:
      result.extend(cand[1])
    
    return result[:3]
    
  def DFS(self, node, candidates):
    if 'word' in node: 
      time, sentence = node['word']
      insort_left(candidates[time], sentence)

    for key in node:
      if key == 'word': continue
      self.DFS(node[key], candidates)
    
    
    
    
  
def runSolution():
  obj = AutocompleteSystem(
    ["i love you", "island", "iroman", "i love leetcode"], 
    [5, 3, 2, 2]
  );
  print(obj.input("i"))    # return ["i love you", "island", "i love leetcode"]. There are four sentences that have prefix "i". Among them, "ironman" and "i love leetcode" have same hot degree. Since ' ' has ASCII code 32 and 'r' has ASCII code 114, "i love leetcode" should be in front of "ironman". Also we only need to output top 3 hot sentences, so "ironman" will be ignored.
  print(obj.input(" "))    # return ["i love you", "i love leetcode"]. There are only two sentences that have prefix "i ".
  print(obj.input("a"))    # return []. There are no sentences that have prefix "i a".
  print(obj.input("#"))    # return []. The user finished the input, the sentence "i a" should be saved as a historical sentence in system. And the following input will be counted as a new search.
  print(obj.input("i"))
  print(obj.input(" "))
  print(obj.input("a"))
  print(obj.input("#"))
  print(obj.input("i"))
  pass
runSolution()


