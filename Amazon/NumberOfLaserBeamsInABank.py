'''

  2125. Number of Laser Beams in a Bank

'''


class Solution:
  def numberOfBeams(self, bank):
    result = 0
    prev = 0
    
    for row in bank:
      count = row.count('1')
      if count:
        result += prev * count
        prev = count
      
    return result


def runSolution():
  solution = Solution()
  print(solution.numberOfBeams(["011001","000000","010100","001000"]))
  print(solution.numberOfBeams(["000","111","000"]))
  pass
runSolution()