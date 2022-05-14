'''

  355. Design Twitter

'''

from collections import defaultdict, deque
import heapq
from itertools import count
import itertools

class Twitter:
  def __init__(self):
      self.count = 0
      self.tweetMap = defaultdict(list)
      self.followMap = defaultdict(set)
        
  def postTweet(self, userId: int, tweetId: int):
      self.tweetMap[userId].append([self.count, tweetId])
      self.count -= 1

  def getNewsFeed(self, userId: int):
      res = []
      minHeap = [] 
      
      self.followMap[userId].add(userId)
      for followeeId in self.followMap[userId]:
          if followeeId in self.tweetMap:
              index = len(self.tweetMap[followeeId]) - 1
              count, tweetId = self.tweetMap[followeeId][index]
              heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])

      while minHeap and len(res) < 10:
          count, tweetId, followeeId, index = heapq.heappop(minHeap)
          res.append(tweetId)
          if index >= 0:
              count, tweetId = self.tweetMap[followeeId][index]
              heapq.heappush(minHeap, [count, tweetId, followeeId, index - 1])
      return res

  def follow(self, followerId: int, followeeId: int):
      self.followMap[followerId].add(followeeId)

  def unfollow(self, followerId: int, followeeId: int):
      if followeeId in self.followMap[followerId]:
          self.followMap[followerId].remove(followeeId)
    
def runSolution():
  # twitter = Twitter()
  # twitter.postTweet(1, 5)
  # print(twitter.getNewsFeed(1))
  # twitter.follow(1, 2)
  # twitter.postTweet(2, 6)
  # print(twitter.getNewsFeed(1))
  # twitter.unfollow(1, 2)
  # print(twitter.getNewsFeed(1))
  
  twitter2 = Twitter()
  twitter2.postTweet(1, 5)
  twitter2.postTweet(1, 3)
  twitter2.postTweet(1, 101)
  twitter2.postTweet(1, 13)
  twitter2.postTweet(1, 10)
  twitter2.postTweet(1, 2)
  twitter2.postTweet(1, 94)
  twitter2.postTweet(1, 505)
  twitter2.postTweet(1, 333)
  twitter2.postTweet(1, 22)
  twitter2.postTweet(1, 11)
  print(twitter2.getNewsFeed(1))
  pass
runSolution()