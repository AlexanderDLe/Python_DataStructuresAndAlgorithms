'''
  Question on AWS power consumption, given BootingPower[i], processingPower[i], powerMax.

  For maximum utilization, the data center wishes to group these processors into clusters. 

  Clusters can only be formed of processors located adjacent to each other. For example, 
  processors 2,3,4,5 can form a cluster, but 1,3,4 cannot.

  Net power consumption = maximum booting power among the k processors + (sum of processing power of processors)*k.
  A cluster is said to be sustainable if it's net power consumption does not exceed a given threshold value powerMax.

  bootingPower = [3,6,1,3,4]
  processingPower = [2,1,3,4,5]
  powerMax = 25

  If k = 2, any adjacent pair can be choosen.   
  maxBootingPower = max(4,5)
  sumOfProcessingPower = sum(4,5)

  The highest usage is the pair [4,5] with net power consumption.
  maxBootingPower + (sumOfProcessingPower * k) = netPowerConsumption
  4 + (4 + 5)2 = 
  22
  
  22 < powerMax: 22 < 25 is true.

  Next, try k = 3. Group the first 3 processors together as:
  Max booting power = max(3,6,1)
  Sum of processing power = 2 + 1+ 3 = 6
  Net power consumption = 6 + 63 = 24 <= powerMax

  ------------------------------------------------------------------------------------------

  Sliding Window for the sumOfProcessingPower and k.
  Monotonic Queue for the maxBootPower

  var ui_url = 'http://192.168.1.14:3000/ui-react/discover/now';
'''

def powerConsumption(bootingPower, processingPower, powerMax):
  maxQ = []
  getMaxQVal = lambda: bootingPower[maxQ[0]]
  getMaxQEnd = lambda: bootingPower[maxQ[-1]]

  result = 0
  n = len(bootingPower)
  k = 1

  while k <= n:
    windowSum = 0
    L = 0
    R = 0

    while R < n:
      bootPower = bootingPower[R]
      procPower = processingPower[R]

      while maxQ and bootPower > getMaxQEnd(): maxQ.pop()
      maxQ.append(R)
      R += 1

      windowSum += procPower
      windowLen = R - L

      if windowLen == k:
        netPower = getMaxQVal() + (windowSum * k)
        if netPower <= powerMax: result = max(result, k)

        windowSum -= processingPower[L]
        if L == maxQ[0]: maxQ.pop(0)

    k += 1
      
  return result







print(powerConsumption([3,6,1,3,4], [2,1,3,4,5], 25))
print(powerConsumption([3,6,1,3,4], [2,1,3,4,5], 50))