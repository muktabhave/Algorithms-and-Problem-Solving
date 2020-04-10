def BuySellStockMultiple(a):
    
    n=len(a)
    profit=0
    l=list()
    if(n==1):
        return
    
    i=0
    while(i<n-1):
        
        while(i<n-1 and a[i+1]< a[i]):
            i+=1
        
        if(i==n-1):
            break
        
        buy=i
        buyval=a[i]
        i+=1
        
        while(i<n and a[i]> a[i-1]):
            i+=1
        
        sell=i-1
        sellval=a[i-1]
        l.append(buyval)
        l.append(sellval)
        profit=profit+(sellval-buyval)
    
    return profit

if(__name__=="__main__"):
    print(BuySellStock([8,2,3,6,5,7]))
