'''

  Calculate the total wait time for a customer C to speak to an agent given N agents, 
  M customers, and T[] time for an agent to serve a customer. 
  
  T[i] represents the amount of time it takes for an agent i to serve one customer. 
  One agent can serve one customer at a time. All N agents can serve concurrently. 
  The customer chooses the agent with the lowest wait time.


  Agents     =  2  5
  Customers  =  1  2
  
  Customer C will have to wait for both customers 1 & 2.
  The customer will access the first available agent.
  
  2 -> 5 -> 2 -> 2

'''


import heapq


class Solution1:
  def calculateWaitTime(self, agents, customers, agentTimes):
    W = [0] * len(agentTimes)

    for _ in range(customers):
      min = float('inf')
      agent = -1
      
      for j in range(agents):
        if (W[j] < min):
          min = W[j]
          agent = j
      W[agent] += agentTimes[agent]
      print(W)

    C_time = 12345
    C_agent = -1
    for j in range(agents):
      if (W[j] < C_time):
        C_time = W[j]
        C_agent = j
        
    print(f"C_time: {C_time}, C_agent: {C_agent}")

class Solution:
  def calculateWaitTime(self, agents, customers, agentTime):
    minHeap = []
    
    for i in range(agents):
      heapq.heappush(minHeap, (0, i)) # (time, agent index)
    
    for _ in range(customers):
      time, agent = heapq.heappop(minHeap)
      heapq.heappush(minHeap, (time + agentTime[agent], agent))
    
    print(minHeap[0])
      
  
  
  
def runSolution():
  solution = Solution()
  print(solution.calculateWaitTime(2, 4, [2,5]))
  pass
runSolution()
