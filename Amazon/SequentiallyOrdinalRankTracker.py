'''

  2102. Sequentially Ordinal Rank Tracker

'''

import heapq


class TopNode(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def __lt__(self, other):
    if self.score == other.score: return self.name > other.name
    return self.score < other.score

class BotNode(object):
  def __init__(self, name, score):
    self.name = name
    self.score = score
  def __lt__(self, other):
    if self.score == other.score: return self.name < other.name
    return self.score > other.score

class SORTracker:
  def __init__(self):
    self.top = []
    self.bot = []
    self.q = 0

  def add(self, name, score):
    heapq.heappush(self.top, TopNode(name, score))
    
    while len(self.top) > self.q:
      node = heapq.heappop(self.top)
      currName, currScore = node.name, node.score
      heapq.heappush(self.bot, BotNode(currName, currScore))

  def get(self):
    node = heapq.heappop(self.bot)
    currName, currScore = node.name, node.score
    self.q += 1
    heapq.heappush(self.top, TopNode(currName, currScore))
    return currName

def runSolution():
  tracker = SORTracker();     # Initialize the tracker system.
  tracker.add("bradford", 2); # Add location with name="bradford" and score=2 to the system.
  tracker.add("branford", 3); # Add location with name="branford" and score=3 to the system.
  
  tracker.get();              # The sorted locations, from best to worst, are: branford, bradford.
                              # Note that branford precedes bradford due to its higher score (3 > 2).
                              # This is the 1st time get() is called, so return the best location: "branford".
                              
  tracker.add("alps", 2);     # Add location with name="alps" and score=2 to the system.
  
  tracker.get();              # Sorted locations: branford, alps, bradford.
                              # Note that alps precedes bradford even though they have the same score (2).
                              # This is because "alps" is lexicographically smaller than "bradford".
                              # Return the 2nd best location "alps", as it is the 2nd time get() is called.
                              
  tracker.add("orland", 2);   # Add location with name="orland" and score=2 to the system.
  tracker.get();              # Sorted locations: branford, alps, bradford, orland.
                              # Return "bradford", as it is the 3rd time get() is called.
                              
  tracker.add("orlando", 3);  # Add location with name="orlando" and score=3 to the system.
  tracker.get();              # Sorted locations: branford, orlando, alps, bradford, orland.
                              # Return "bradford".
                              
  tracker.add("alpine", 2);   # Add location with name="alpine" and score=2 to the system.
  tracker.get();              # Sorted locations: branford, orlando, alpine, alps, bradford, orland.
                              # Return "bradford".
                              
  tracker.get();              # Sorted locations: branford, orlando, alpine, alps, bradford, orland.
runSolution()