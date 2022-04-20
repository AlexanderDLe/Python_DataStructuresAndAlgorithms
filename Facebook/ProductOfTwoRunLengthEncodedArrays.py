'''

  1868. Product of Two Run-Length Encoded Arrays

'''


def findRLEArrayTooSlow(encoded1, encoded2):
  def expand(encoded):
    nums = []
    for val, freq in encoded:
      arr = [val] * freq
      nums = nums + arr
    return nums

  def getProduct(nums1, nums2):
    product = []
    for i in range(len(nums1)):
      val = nums1[i] * nums2[i]
      product.append(val)
    return product

  def compress(product):
    n = len(product)
    compressed = []

    pair = [product[0], 1]

    for i in range(1, n):
      val = product[i]
      if val == product[i - 1]:
        pair[1] += 1
      else:
        compressed.append(pair)
        pair = [val, 1]

    compressed.append(pair)

    return compressed
  
  nums1 = expand(encoded1)
  nums2 = expand(encoded2)
  product = getProduct(nums1, nums2)
  return compress(product)

def findRLEArray(encoded1, encoded2):
  result = []

  n1, n2 = len(encoded1), len(encoded2)
  p1, p2 = 0, 0

  while p1 < n1 and p2 < n2:
    val1, freq1 = encoded1[p1]
    val2, freq2 = encoded2[p2]

    product = val1 * val2
    minFreq = min(freq1, freq2)

    encoded1[p1][1] -= minFreq
    encoded2[p2][1] -= minFreq

    if encoded1[p1][1] == 0: p1 += 1
    if encoded2[p2][1] == 0: p2 += 1

    if result and result[-1][0] == product:
      result[-1][1] += minFreq
    else:
      result.append([product, minFreq])

  return result

print(findRLEArray(encoded1 = [[1,3],[2,3]], encoded2 = [[6,3],[3,3]]))
print(findRLEArray(encoded1 = [[1,3],[2,1],[3,2]], encoded2 = [[2,3],[3,3]]))