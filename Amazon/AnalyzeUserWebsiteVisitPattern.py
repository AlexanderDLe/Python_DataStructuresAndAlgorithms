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

import os, sys
currentdir = os.path.dirname(os.path.realpath(__file__))
parentdir = os.path.dirname(currentdir)
sys.path.append(parentdir)
from functools import cmp_to_key
from _utils import printDict


def buildNameToHistory(username, timestamp, website, n):
  nameToPattern = {}
  
  for i in range(n):
    name, time, site = username[i], timestamp[i], website[i]
    if name not in nameToPattern: nameToPattern[name] = []
    nameToPattern[name].append((time, site))

  return nameToPattern


def buildPatternFrequency(nameToPattern):
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

def compare(a, b):
  aCode, bCode = a[0], b[0]
  aFreq, bFreq = a[1]['frequency'], b[1]['frequency']

  if aFreq == bFreq:
    if aCode < bCode: return -1
    else            : return 1

  return bFreq - aFreq

def mostVisitedPattern(username, timestamp, website):
  n = len(timestamp)

  nameToTimeHistory = buildNameToHistory(username, timestamp, website, n)
  patternFrequency  = buildPatternFrequency(nameToTimeHistory)
  printDict(patternFrequency)

  sortedItems = sorted(patternFrequency.items(), key=cmp_to_key(compare))
  return sortedItems[0][1]['pattern']

print(mostVisitedPattern([
  "joe","joe","joe","james","james","james","james","mary","mary","mary"], 
  [1,2,3,4,5,6,7,8,9,10], 
  ["home","about","career","home","cart","maps","home","home","about","career"]
))
print(mostVisitedPattern(
  ["ua","ua","ua","ub","ub","ub"], 
  [1,2,3,4,5,6], 
  ["a","b","a","a","b","c"]
))
print(mostVisitedPattern(
  ["dowg","dowg","dowg"],
  [158931262,562600350,148438945],
  ["y","loedo","y"]
))
print(mostVisitedPattern(
  ["h",         "eiy",        "cq",       "h",       "cq",       "txldsscx",  "cq",      "txldsscx",  "h",        "cq",       "cq"],
  [527896567,   334462937,     517687281,  134127993,  859112386, 159548699,   51100299,   444082139,  926837079,  317455832,  411747930],
  ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"]
))

