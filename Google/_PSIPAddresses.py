'''
  Given an input table with IP address ranges and cities, return the city that falls within the IP range.

  Ex:
  1.0.0.1, 1.0.0.10 LA
  5.0.0.255, 7.0.1.0 NY
  200.0.0.0 210.1.2.3 DC
  
'''


from collections import defaultdict, deque


class Solution:
  def assignIP(self, addresses, queries):
    self.array = self.buildArray(addresses)
    ans = []
    
    for query in queries:
      ans.append(self.binarySearch(query))
    
    return ans
    
  def binarySearch(self, query):
    L, R = 0, len(self.array) - 1
    ip = self.convertIPToInt(query)
    
    while L <= R:
      M = L + (R - L)//2
      fr, to, city = self.array[M]
      
      if fr <= ip <= to: return city
      if ip < fr: R = M - 1
      else      : L = M + 1
    
    return 'Empty'
    
  def buildArray(self, addresses):
    array = []
    
    for fr, to, city in addresses:
      fr = self.convertIPToInt(fr)
      to = self.convertIPToInt(to)
      array.append((fr, to, city))
    
    array.sort()
    return array
    
  def convertIPToInt(self, ip):
    m = ''
    for i in ip.split('.'):
        m += (3-len(i))*'0' + i
    return int(m)


def runSolution():
  solution = Solution()
  print(solution.assignIP(
    addresses = [
      ['1.0.0.1', '1.0.0.10', 'LA'],
      ['5.0.0.255', '7.0.1.0', 'NY'],
      ['200.0.0.0', '210.1.2.3', 'DC']
    ],
    queries = ['1.0.0.4', '1.0.1.0', '5.0.3.0','6.0.0.0','20.0.0.0','205.0.0.0']
    ))
  pass
runSolution()