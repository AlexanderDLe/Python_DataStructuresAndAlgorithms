'''

  1570. Dot Product of Two Sparse Vectors

'''


class SparseVector:
  def __init__(self, nums) -> None:
    self.indexToVal = {}
    for i, num in enumerate(nums):
      if num != 0: self.indexToVal[i] = num

  def dotProduct(self, vec):
    result = 0
    Aindexes, Bindexes = self.indexToVal, vec.indexToVal

    for i in Aindexes:
      if i not in Bindexes: continue
      result += (Aindexes[i] * Bindexes[i])

    return result
      


v1 = SparseVector([1,0,0,2,3])
v2 = SparseVector([0,3,0,4,0])
print(v1.dotProduct(v2))