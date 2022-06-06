'''
  Amazon ships millions of packages regularly .There are a number of parcels that need 
  to be shipped .Compute the minimum possible sum of transportation costs incurred in 
  the shipment of additional parcels in the following scenario .

  A fully loaded truck carries K parcels
  It is most efficient for the truck to be fully loaded .
  There are a number of parcels with unique Id that ranges from 1 through infinity
  The parcel id is also the cost to ship that parcel
  Given the parcel id's which are already added in the shipment , find the minimum possible 
  cost of the shipping the items added to complete the load .The items added to complete 
  the load. Example:

  parcels = [2,3,6,10,11] k = 9

  parcel id's range from 1 from 1 through infinity .After reviewing the current manifest 
  the remaining parcel to choose from are [1,4,5,7,8,9,12,12,...]. There are 5 parcels 
  already on the truck and it can carry k = 9 parcels when fully loaded . Choose 4 more 
  packages to include [ 1,4,5,7].Their shipping cost is 1 + 4 + 5 + 7 = 17, which is minimal. 
  Return 17  

  ----------------------------------------------------------------

'''

def maxCost(parcels, k):
  parcelSet = set(parcels)
  
  k -= len(parcels)
  cost = 0
  i = 1
  while k > 0:
    if i not in parcelSet:
      cost += i
      k -= 1

    i += 1


  return cost


print(maxCost([2,3,6,10,11], 9))