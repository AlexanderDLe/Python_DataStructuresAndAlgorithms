'''

  Problem: Given an input string, return an output string such that all the lower case 
  characters should be sorted. Indices of non-lower case characters should remain the 
  same as in the original input string.

  Example:
  Input  -> 'Test@123 Google'
  Output -> 'Teeg@123 Gloost'

  _____________________________________________________________________________

  Strategy:
  'Test@123 Google' 

  1. Convert into array -> [T, e, s, t @, 1, 2, 3, ‘ ‘, G, o, o, g, l, e]
  2. Loop and increment lower case chars in alphabet array to store which chars
     are lower cased and frequency of the char:

      a  b  c  d  e  f  g
    [0, 0, 0, 0, 2, 0, 1, etc...]
    
  3. Traverse input array and for every lower case character, we place the earliest valid lower-case char found in alphabet array.

  4. Join and return string.

'''

class Solution:
  def sortLowerCase(self, s):	
    arr = list(s)
    alphabetArr = [0] * 26
    
    for char in arr:
      charCode = self.getCharCode(char)
      if 0 <= charCode <= 25:
        alphabetArr[charCode] += 1
  
    alphaIndex = 0
    for i, char in enumerate(arr):
      charCode = self.getCharCode(char)
      
      if 0 <= charCode <= 25:
        while alphabetArr[alphaIndex] == 0:
          alphaIndex += 1
        
        arr[i] = self.getCharFromCode(alphaIndex)
        alphabetArr[alphaIndex] -= 1
    
    return ''.join(arr)
  
  def getCharCode(self, char):
    return ord(char) - ord('a')
  
  def getCharFromCode(self, code):
    return chr(code + ord('a'))

  
def runSolution():
  solution = Solution()
  print(solution.sortLowerCase('Test@123 Google'))
  pass
runSolution()