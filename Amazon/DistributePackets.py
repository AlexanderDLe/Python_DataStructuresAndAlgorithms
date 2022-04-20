'''

  Given channels = k, with a List<int> packets and length of each pack, 
  distribute the packs, ensure the sum of all channels median is max.

'''

import heapq

def distributePackets(channels, packets):
  packets.sort(reverse=True)
  heap = [0] * channels
  maxSum = 0

  for packet in packets:
    smallestChannel = heapq.heappop(heap)
    updatedChannel  = smallestChannel + packet
    maxSum = max(maxSum, updatedChannel)

    heapq.heappush(heap, updatedChannel)
  print(heap)
  return maxSum
  

print(distributePackets(3, [1,2,3,4,5,6,7,8,9]))