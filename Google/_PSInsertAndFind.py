'''
  I have been asked int google telephonic interview this simple question but unable to resolve it in given 45 time limit,
  The question is: U need to design structure in which it will nee to implement following 2 methods :

  public void insertOrReplace(long index, long number)
  public long findSmallestIndex(long number)
  
  so the first one is to insert the number on the index given by the user, index can be any number of long type and if at the same index another number comes it will replace that number
  2nd method is need to be implemented int which user will be given any number and we need to return the smallest index of that number
  
  Ex:
  
  index->number sequence
  2->100
  1->100
  3->100
  5->100
  if any user does findSmallestIndex(100) , output will be 1
  2-> 200
  if new number 200 comes at index 2 then 100 will be present only at indexs 1,3 &5 and 2nd index will be removed.
  
  Please help.
  I have told the approach after getting hint from my interviewer, but not able to code it due to time limit .
  I just told them that I will use 2 hashmaps one for index->number and another for number->tree set of indexes->I will use treeset here because it will store the indexes in sorted order
  I dont know If I will get the chance for 2nd round of interview or not. I am very upset.
'''


from collections import defaultdict
import heapq

class Solution:
  def __init__(self):
    self.indexMap = defaultdict(int)
    self.heapMap = defaultdict(list)
  
  def insertOrReplace(self, index, number):
    self.indexMap[index] = number
    heapq.heappush(self.heapMap[number], index)

  def findSmallestIndex(self, number):
    arr = self.heapMap[number]
    
    while arr:
      top = arr[0]
      if self.indexMap[top] == number: return top
      else: heapq.heappop(arr)
    
    return -1


def runSolution():
  solution = Solution()
  solution.insertOrReplace(2, 100)
  solution.insertOrReplace(1, 100)
  solution.insertOrReplace(3, 100)
  solution.insertOrReplace(5, 100)
  print(solution.findSmallestIndex(100))
  solution.insertOrReplace(1, 200)
  print(solution.findSmallestIndex(100))
  print(solution.findSmallestIndex(200))
  pass
runSolution()