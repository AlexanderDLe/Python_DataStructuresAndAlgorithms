'''

  1268. Search Suggestion System

'''

def buildTrie(products):
  trie = {'indexes': []}

  for i, product in enumerate(products):
    node = trie
    node['indexes'].append(i)

    for char in product:
      if char not in node: node[char] = {'indexes': []}
      node = node[char]
      node['indexes'].append(i)    

  return trie


def suggestProducts(products, searchWord):
  products.sort()
  node = buildTrie(products)
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


# print(suggestProducts(["mobile","mouse","moneypot","monitor","mousepad"], "mouse"))
# print(suggestProducts(["havana"], "havana"))
# print(suggestProducts(["havana"], "tatiana"))
# print(suggestProducts(["bags","baggage","banner","box","cloths"], "bags"))