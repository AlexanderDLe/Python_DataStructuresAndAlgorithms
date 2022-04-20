'''

  347. Top K Frequent Elements

'''

def topKFrequentRef(nums, k):
  buckets = [[] for x in range(len(nums) + 1)]
  numberCount = {}
  
  for num in nums: numberCount[num] = numberCount.get(num, 0) + 1

  for num, freq in numberCount.items():
    buckets[freq].append(num)

  flatList = []
  
  for i in range(len(buckets) - 1, -1, -1):
    bucket = buckets[i]
    if bucket == []: continue
    for num in bucket: flatList.append(num)

  return flatList[:k]


def topKFrequent(nums, k):
  buckets = [[] for x in range(len(nums) + 1)]
  freqDict = {}
  
  for num in nums: freqDict[num] = freqDict.get(num, 0) + 1

  for num, freq in freqDict.items(): buckets[freq].append(num)

  flatList = []
  for i in range(len(buckets) - 1, -1, -1):
    bucket = buckets[i]
    if bucket == []: continue
    for num in bucket: flatList.append(num)

  return flatList[:k]

print(topKFrequent([1,1,1,2,2,3], 2))
print(topKFrequent([1, 2], 2))