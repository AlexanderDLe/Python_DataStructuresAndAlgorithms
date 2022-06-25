'''

  1152. Analyze User Website Visit Pattern

  ------------------------------------------------------------------------

  "joe","joe","joe","james","james","james","james","mary","mary","mary"], 
  [1,2,3,4,5,6,7,8,9,10], 
  ["home","about","career","home","cart","maps","home","home","about","career"]

  Organize by name:

  {
    joe:   [home, about, career]
    james: [home, cart, maps, home]
    mary:  [home, about, career]
  }

  Get permutations of all valid pattnerns using nested loops
  In the above example, only james has visited more than 3 so we will use him

  [home, cart, maps]
  [home, cart, home]
  [cart, maps, home]

  Encode then store all valid combinations in a dict.
  Each one will also need a frequency counter

  'home-cart-maps': [home, cart, maps], 1
  'home-cart-home': [home, cart, home], 1
  'cart-maps-home': [cart, maps, home], 1

  Continue doing and populate the array.

'''

from collections import defaultdict
from functools import cmp_to_key

class SolutionRef:
  def buildNameToHistory(self, username, timestamp, website, n):
    nameToPattern = {}
    
    for i in range(n):
      name, time, site = username[i], timestamp[i], website[i]
      if name not in nameToPattern: nameToPattern[name] = []
      nameToPattern[name].append((time, site))

    return nameToPattern


  def buildPatternFrequency(self, nameToPattern):
    frequencyMap = {}

    for name in nameToPattern:
      history = sorted(nameToPattern[name], key=lambda x: x[0])
      seenSet = set()

      for i in range(0, len(history) - 2):
        for j in range(i + 1, len(history) - 1):
          for k in range(j + 1, len(history)):
            encode = f'{history[i][1]}-{history[j][1]}-{history[k][1]}'
            
            if encode not in seenSet:
              if encode not in frequencyMap: frequencyMap[encode] = {'frequency': 1, 'pattern': [history[i][1], history[j][1], history[k][1]]}
              else                         : frequencyMap[encode]['frequency'] += 1
              seenSet.add(encode)
    
    return frequencyMap

  def compare(self, a, b):
    aCode, bCode = a[0], b[0]
    aFreq, bFreq = a[1]['frequency'], b[1]['frequency']

    if aFreq == bFreq:
      if aCode < bCode: return -1
      else            : return 1

    return bFreq - aFreq

  def mostVisitedPattern(self, username, timestamp, website):
    n = len(timestamp)

    nameToTimeHistory = self.buildNameToHistory(username, timestamp, website, n)
    patternFrequency  = self.buildPatternFrequency(nameToTimeHistory)

    sortedItems = sorted(patternFrequency.items(), key=cmp_to_key(self.compare))
    return sortedItems[0][1]['pattern']
  
class Solution:
  def mostVisitedPattern(self, username, timestamp, website):
    userMap = self.buildUserMap(username, timestamp, website)
    patternMap = self.buildPatternMap(userMap)
    patternItems = list(patternMap.items())

    patternItems.sort(key = lambda x: x[0])
    patternItems.sort(key = lambda x: x[1]['freq'], reverse=True)

    return patternItems[0][1]['pattern']
    
    
  def buildPatternMap(self, userMap):
    patternMap = defaultdict(lambda: {'freq': set()})
    
    for user, sites in list(userMap.items()):
      historyLen = len(sites)
      
      for i in range(historyLen):
        for j in range(i + 1, historyLen):
          for k in range(j + 1, historyLen):
            pattern = [sites[i], sites[j], sites[k]]
            patternStr = '-'.join(pattern)
            
            patternMap[patternStr]['freq'].add(user)
            patternMap[patternStr]['pattern'] = pattern
    
    for key in patternMap:
      patternMap[key]['freq'] = len(patternMap[key]['freq'])
    
    return patternMap
  
  def buildUserMap(self, username, timestamp, website):
    arr = []
    for user, time, site in zip(username, timestamp, website):
      arr.append((time, user, site))
    arr.sort()
    
    userMap = defaultdict(list)
    for _, user, site in arr:
      userMap[user].append(site)
    
    return userMap
    

  
def runSolution():
  solution = Solution()
  # print(solution.mostVisitedPattern([
  #   "joe","joe","joe","james","james","james","james","mary","mary","mary"], 
  #   [1,2,3,4,5,6,7,8,9,10], 
  #   ["home","about","career","home","cart","maps","home","home","about","career"]
  # ))
  # print(solution.mostVisitedPattern(
  #   ["ua","ua","ua","ub","ub","ub"], 
  #   [1,2,3,4,5,6], 
  #   ["a","b","a","a","b","c"]
  # ))
  # print(solution.mostVisitedPattern(
  #   ["dowg","dowg","dowg"],
  #   [158931262,562600350,148438945],
  #   ["y","loedo","y"]
  # ))
  # print(solution.mostVisitedPattern(
  #   ["h",         "eiy",        "cq",       "h",       "cq",       "txldsscx",  "cq",      "txldsscx",  "h",        "cq",       "cq"],
  #   [527896567,   334462937,     517687281,  134127993,  859112386, 159548699,   51100299,   444082139,  926837079,  317455832,  411747930],
  #   ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
  # ))
  print(solution.mostVisitedPattern(
    ["him","mxcmo","jejuvvtye","wphmqzn","uwlblbrkqv","flntc","esdtyvfs","nig","jejuvvtye","nig","mxcmo","flntc","nig","jejuvvtye","odmspeq","jiufvjy","esdtyvfs","mfieoxff","nig","flntc","mxcmo","qxbrmo"],
    [113355592,304993712,80831183,751306572,34485202,414560488,667775008,951168362,794457022,813255204,922111713,127547164,906590066,685654550,430221607,699844334,358754380,301537469,561750506,612256123,396990840,60109482],
    ["k","o","o","nxpvmh","dssdnkv","kiuorlwdcw","twwginujc","evenodb","qqlw","mhpzoaiw","jukowcnnaz","m","ep","qn","wxeffbcy","ggwzd","tawp","gxm","pop","xipfkhac","weiujzjcy","x"]
  ))
  pass
runSolution()

