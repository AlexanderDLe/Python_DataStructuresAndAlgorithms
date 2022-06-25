'''

  Q2 : Given a password string, calculate its strength, where strength is equals 
  to the sum of count of distinct characters in all the substrings of that string.

  Example: "aba" -> answer is 9

  All substrings of 'aba'

  a, b, a, ab, ba, aba -> 

  Distinct characters of each substring:

    a   = 1
    b   = 1
    a   = 1
    ab  = 2
    ba  = 2
    aba = 2
  _________
  Total = 9

  -----------------------------------------------------------------------

  TIP: Formula for getting total substring count: (n * (n + 1))/2

  aba -> 3 characters

  3 * (3 + 1) / 2 = 
  3 * (4) / 2 = 
  12 / 2 = 
  6

  -----------------------------------------------------------------------

  Find the contribution of each character

  5 Contributions of a: a, a, ab, ba, aba

  --------------------------------------

  There are 6 total substrings in original substring.

  We can work backward - instead of trying to get a contributions directly,
  we can get the substrings of the segments without a and subtract to original.

  segments without a in aba: -b-

  Here we see the b is the only segment without a.
  The substring count of b is 1: 'b'

  There are 6 total substrings, we can subtract this by the substring segments:
  6 - 1 = 5.

  ---------------------------------------------------------------------------

  Find the contribution of each character

  4 Contributions of b: b, ab, ba, aba

  ---------------------------------------

  Let continue working in reverse:

  segments without a in aba: a-a

  There are two segments without a b in them.
  Since they are only 1 character each, the substring count in each is only 1.

  There are 6 total substrings, we can subtract this by the substring segments:
  6 - 2 = 4

  ---------------------------------------------------------------------------

  5 = 4 = 9

'''

import string

class Solution:
  def passwordStrength(self, str):
    totalSubstrings = self.getSubstrCount(len(str))
    total = 0

    for char in string.ascii_lowercase:
      if char not in str: continue
      total += (totalSubstrings - self.getSegmentCounts(char, str))
      
    return total


  def getSegmentCounts(self, char, str):
    segmentsTotal = 0
    segmentLen = 0

    for i in range(len(str)):
      curr = str[i]

      if curr == char:
        segmentsTotal += self.getSubstrCount(segmentLen)
        segmentLen = 0
      else:
        segmentLen += 1

    segmentsTotal += self.getSubstrCount(segmentLen)
    return segmentsTotal
  
  def getSubstrCount(self, n):
    return (n * (n + 1)) / 2
  
  
  
def runSolution():
  solution = Solution()
  print(solution.passwordStrength('aba'))
  pass
runSolution()