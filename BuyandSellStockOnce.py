import math

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        minval= math.inf
        maxprofit= 0
        
        for i in range (len(prices)):
            
            if(prices[i]< minval):
                
                minval= prices[i]
            
            else:
                
                if((prices[i]-minval)> maxprofit):
                    
                    maxprofit= prices[i]-minval
                    
        return maxprofit



# Second Approach
#def BuyandSellStockOnce(a):
    
#     minele=a[0]
#     for i in range (1, len(a)):
#         if (a[i]< minele):
#             minele=a[i]
#             buyidx = i
    
#     maxele= minele
    
#     for j in range (buyidx+1,len(a)):
#         if(a[j]> maxele):
#             maxele= a[j]
#             #sellidx= j
#     return (maxele- minele)

# if (__name__=="__main__"):
#     print(BuyandSellStock([7,1,5,3,6,4]))
