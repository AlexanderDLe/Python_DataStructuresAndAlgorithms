def printMatrix(matrix):
  for i in matrix:
    print(' |\t'.join(map(str, i)))

def printDict(dict):
  longestStr = max(dict.keys(), key=len)
  maxLen = len(longestStr)
  
  print('{')
  for key in dict:
    currLen = len(key)
    lenDiff = maxLen - currLen
    print('  ' + key + (' ' * lenDiff) + ': ' + str(dict[key]))
  print('}')

def printVerticalList(list):
  for item in list:
    print(item)


def printLinkedList(node):
  result = ''
  while node != None:
    node.val = str(node.val)
    result += node.val + ' -> '
    node = node.next

  print(result)