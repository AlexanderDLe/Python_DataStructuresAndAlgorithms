'''

  We have an array of N positive elements. 
  
  We can perform M operations on this array. In each operation we have to select a 
  subarray(contiguous) of length W and increase each element by 1. Each element of 
  the array can be increased at most K times. We have to perform these operations 
  such that the minimum element in the array is maximized.

  1 <= N, W <= 10^5

  1 <= M, K <= 10^5

  ---------------------------------------------------------------------------------

  Example from another comment: 
  
  a = [1 4 2 9], W = 3, M = 2. 
  
  Let's say our desired minimum is 5. Then b = [4, 1, 3, 0]; 
  the leftmost index, i = 0, has b = 4.
  
  We need to add to this 4 times to get it equal to 5, 
  but we can't do that because M = 2, and so desMin = 5 is not attainable. 
  
  However, try desMin = 3 instead; then b = [2, 0, 1, 0], and M = 2 is enough. 
  
  We add to [0, 2] exactly twice, and in doing that we get both b[0] and b[2] 
  down below 1, so desMin = 3 is feasible.

  So how will we use isFeasible and getAdds? Think about what desMin tells us; if isFeasible(desMin) is false, then isFeasible(v) is definitely false for all v > desMin as well, so we should only concern ourselves with values below desMin. On the other hand, if isFeasible(desMin) is true, then it's definitely true for all v < desMin as well, and it might be true for values greater than desMin too. This sets us up well for binary search in the minimum range [mi, mi + M].

'''
