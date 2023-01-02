'''

  1268. Search Suggestion System

'''


class SolutionRef:
  def buildTrie(self, products):
    trie = {'indexes': []}

    for i, product in enumerate(products):
      node = trie
      node['indexes'].append(i)

      for char in product:
        if char not in node: node[char] = {'indexes': []}
        node = node[char]
        node['indexes'].append(i)    

    return trie


  def suggestedProducts(self, products, searchWord):
    products.sort()
    node = self.buildTrie(products)
    invalid = False
    result = []

    for char in searchWord:
      if char not in node or invalid == True:
        invalid = True
        result.append([])
        continue

      node = node[char]
      indexes = node['indexes'][0: 3]
      result.append(list(map(lambda i: products[i], indexes)))

    return result
  
class Solution:
  def suggestedProducts(self, products, searchWord):
    products.sort()
    node = self.buildTrie(products)
    result = []
    invalid = False
    
    for char in searchWord:
      if invalid or char not in node:
        invalid = True
        result.append([])
        continue
    
      node = node[char]
      res = []
      
      for i in node['indices']:
        res.append(products[i])
      
      result.append(res)
      
    
    return result
  
  
  def buildTrie(self, products):
    trie = {'indices': []}
    
    for i, product in enumerate(products):
      node = trie
      for char in product:
        node = node.setdefault(char, {'indices': []})
        if len(node['indices']) < 3: node['indices'].append(i)
    
    return trie

  
def runSolution():
  solution = Solution()
  print(solution.suggestedProducts(
    ["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
  print(solution.suggestedProducts(
    ["havana"], "havana"))
  print(solution.suggestedProducts(
    ["bags","baggage","banner","box","cloths"], "bags"))
  pass
runSolution()