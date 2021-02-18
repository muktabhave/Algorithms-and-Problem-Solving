def BubbleSort(a):
    
    n=len(a)-1
    
    for i in range(n):
        
        for j in range(n-i):
            if(a[j]>a[j+1]):
                temp=a[j]
                a[j]=a[j+1]
                a[j+1]=temp

    return a

if (__name__=="__main__"):
    
    print(BubbleSort([2,10,5,8,3]))
