'''
  https://leetcode.com/discuss/interview-question/1874764/throttling-gateway

  Non-critical requests are routed through a throttling gateway to ensure that
  the network is no choked by non-essential requests.

  The gateway as the following limits:

  1. The number of transactions in any given second cannot exceed 3.

  2. The number of transactions in any given 10-second period cannot exceed 20
     A 10-second period includes all requests arriving from any time 
     max(1, T-9) to T (inclusive) for any valid time T

  3. The number of transations in any given minute cannot exceed 60. Similar to above,
     1 minute is from max(1, T-59) to T

  Any request that exceeds any of the above limits will be dropped by the gateway.
  Given the times at which different requests arrive sorted ascending, find how many
  requests will be dropped.

  Note: Even if a request is dropped, it is still considered for future calculations.
        Although, if a request is dropped due to multiple violations, it is still 
        only counted once.

  --------------------------------------------------------------------------------------

  Example:

  n = 7
  requestTimes = [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]

  Request 1 - Not Dropped
  Request 1 - Not Dropped
  Request 1 - Not Dropped
  Request 1 - Dropped. At most 3 requests are allowed in one second
  ...
  No requests will be dropped until 6 as all comes at an allowed rate of 3 requests per second
  and the 10-second clause is also not violated.
  ...
  Request 7 - Not Dropped. At most 20 requests are allowed in 10 seconds.
  Request 7 - Dropped. At most 20 requests are allowed in 10 seconds.
  Request 7 - Dropped. At most 20 requests are allowed in 10 seconds.
  Request 7 - Dropped. At most 20 requests are allowed in 10 seconds. Note that 1-second limit is violated here.
  Request 11 - Not Dropped. The 10-second window has now become 2 to 11. Hence the total # of requests in this window is 20 now.
  Request 11 - Dropped. At most 20 requests are allowed in 10 seconds.
  Request 11 - Dropped. At most 20 requests are allowed in 10 seconds.
  Request 11 - Dropped. At most 20 requests are allowed in 10 seconds. Also, at most 3 requests allowed per second.

  Total of 7 requests are dropped.

  --------------------------------------------------------------------------------------

  Strategy: Scan through the requestTimes 3 times, 1 for each of the requirements.
  Keep track of total drops and requests that were dropped to avoid duplication.

  dropped = 0
  prevDrop = {}
  
  1. First, scan for first requirement: 3 requests per second.

  [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
         ^
         | Since this request is identical to request[i - 3], then it is dropped


  2. Then scan for second requirement: 20 requests per second

  [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
                                           ^
                                           | At request 21, we see that it has only been 7 seconds.
                                             Therefore, we drop all these 7s hereafter

  [1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]
                                                  ^
                                                  | At request 24, the 10-second window collapses into 2-11
                                                    We can check i - 20 and see if it is greater than 10 seconds.


'''

import collections


def throttlingGateway(requestTimes):
  dropped = 0
  passed = []

  for i in range(len(requestTimes)):
    currTime = requestTimes[i]

    if   i > 2  and currTime == requestTimes[i - 3]:
      dropped += 1
    
    elif i > 19 and currTime - requestTimes[i - 20] < 10:
      dropped += 1

    elif i > 59 and currTime - requestTimes[i - 60] < 60:
      dropped += 1

    else:
      passed.append(currTime)

  # print(passed)
  return dropped
  
def throttling_gateway(requestTime):
  """
  :type n: int
  :type requestTime: int
  :rtype: int
  """

  pair_value_list = [(1, 3), (10, 20), (60, 60)]
  unique_value_dict = set()
  count_value_dict = collections.Counter(requestTime)
  max_length = max(requestTime)
  presum_value_list = [0] * (max_length + 1)
  res = 0  

  if not requestTime:
      
      return res
  
  for i in range(1, max_length + 1):
      presum_value_list[i] = presum_value_list[i - 1] + count_value_dict[i]

  for state, capacity in pair_value_list:
      window_value = min(state, max_length)
      
      for i in range(max_length - window_value + 1):
          request_value = presum_value_list[i + window_value] - presum_value_list[i]
          temp_value = max(0, request_value - capacity)
          
          for j in range(1, temp_value + 1):
              unique_value_dict.add(presum_value_list[i + window_value] - j)
  
  res = len(unique_value_dict)
  
  return res


print(throttlingGateway([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(throttlingGateway([1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6,7,7,7,7,7,10,10,10,10,10,10,10,10,10]))
print(throttlingGateway([1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]))

print(throttling_gateway([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]))
print(throttling_gateway([1,1,1,1,1,1,1,1,1,1,1,1,1,4,5,6,7,7,7,7,7,10,10,10,10,10,10,10,10,10]))
print(throttling_gateway([1,1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,11,11,11,11]))