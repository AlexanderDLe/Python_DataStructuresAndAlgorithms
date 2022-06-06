'''

  68. Text Justification

'''


from collections import deque

class Solution:
  def fullJustify(self, words, maxWidth):
    self.maxWidth = maxWidth
    result, curr, currLen = [], [], 0
    
    for word in words:
      if currLen + len(curr) + len(word) <= maxWidth:
        curr.append(word)
        currLen += len(word)
      else:
        result.append(self.centerJustify(curr, currLen))
        curr = [word]
        currLen = len(word)
  
    finalStr = ' '.join(curr)
    finalStr += ' ' * (maxWidth - len(finalStr))
    result.append(finalStr)
    
    return result
  
  def centerJustify(self, curr, currLen):
    size = max(1, len(curr) - 1)
    
    for i in range(self.maxWidth - currLen):
      index = i % size
      curr[index] += ' '
    
    return ''.join(curr)
    
  def centerJustify2(self, array):
    letters = 0
    for word in array:
      letters += len(word)
    
    spacesRequired = self.maxWidth - letters
    gaps = len(array) - 1 if len(array) > 1 else 1
    
    evenSpaces = spacesRequired // gaps
    leftovers  = spacesRequired  % gaps
    res = ''
    
    gapArr = [(' ' * evenSpaces)] * gaps
    i = 0
    while leftovers:
      gapArr[i] += ' '
      leftovers -= 1
      i += 1
      
    i = 0
    while i < len(array):
      res += array[i]
      if i < len(gapArr): res += str(gapArr[i])
      i += 1
    
    return res
    
    
    
  

def runSolution():
  solution = Solution()
  print(solution.fullJustify(
    words = ["This", "is", "an", "example", "of", "text", "justification."], 
    maxWidth = 16))
  print(solution.fullJustify(
    words = ["What","must","be","acknowledgment","shall","be"], 
    maxWidth = 16))
  print(solution.fullJustify(
    words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], 
    maxWidth = 20))
  
  pass
runSolution()