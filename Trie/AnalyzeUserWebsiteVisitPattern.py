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

from collections import Counter, defaultdict
from functools import cmp_to_key
from itertools import combinations

class Solution:
  def mostVisitedPattern(self, username, timestamp, website):
    users = defaultdict(list)
    sortedZip = sorted(zip(username, timestamp, website), key=lambda x: x[1])
    
    for user, _, site in sortedZip:
      users[user].append(site)
      
    patterns = Counter()
    
    for user, sites in list(users.items()):
      allPatterns = set(combinations(sites, 3))
      for pattern in allPatterns: patterns[pattern] += 1
      
    print(patterns)
    
    

  
def runSolution():
  solution = Solution()
  print(solution.mostVisitedPattern([
    "joe","joe","joe","james","james","james","james","mary","mary","mary"], 
    [1,2,3,4,5,6,7,8,9,10], 
    ["home","about","career","home","cart","maps","home","home","about","career"]
  ))
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
  # print(solution.mostVisitedPattern(
  #   ["him","mxcmo","jejuvvtye","wphmqzn","uwlblbrkqv","flntc","esdtyvfs","nig","jejuvvtye","nig","mxcmo","flntc","nig","jejuvvtye","odmspeq","jiufvjy","esdtyvfs","mfieoxff","nig","flntc","mxcmo","qxbrmo"],
  #   [113355592,304993712,80831183,751306572,34485202,414560488,667775008,951168362,794457022,813255204,922111713,127547164,906590066,685654550,430221607,699844334,358754380,301537469,561750506,612256123,396990840,60109482],
  #   ["k","o","o","nxpvmh","dssdnkv","kiuorlwdcw","twwginujc","evenodb","qqlw","mhpzoaiw","jukowcnnaz","m","ep","qn","wxeffbcy","ggwzd","tawp","gxm","pop","xipfkhac","weiujzjcy","x"]
  # ))
  pass
runSolution()

