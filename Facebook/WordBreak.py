'''

  140. Word Break II

  --------------------------------------------------

  dict = {cat, cats, and, sand, dog}

  catsanddog
    ^
  sanddog
     ^
  dog
    ^
  'cat sand dog'

  --------------------------------------------------

  dict = {cat, cats, and, sand, dog}

  catsanddog
     ^

  anddog
    ^
  dog
    ^
  'cats and dog'
  
'''
def buildTrie(wordDict):
  trie = {}

  for word in wordDict:
    node = trie
    for char in word:
      if char not in node: node[char] = {}
      node = node[char]
    node['word'] = word

  return trie

def wordBreak(s, wordDict):
  n = len(s)
  trie = buildTrie(wordDict)
  result = []
  
  def backtrack(index, sentence, node):
    if index == n:
      result.append(' '.join(sentence))
      return

    for i in range(index, n):
      char = s[i]
      if char not in node: break

      node = node[char]
      if 'word' in node:
        sentence.append(node['word'])
        backtrack(i + 1, sentence, trie)
        sentence.pop()
    
  backtrack(0, [], trie)
  return result


print(wordBreak(s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]))
# print(wordBreak(s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]))
# print(wordBreak(s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]))