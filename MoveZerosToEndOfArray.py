def moveZeroes(a):
    n=len(a)
    j=0
    for i in range(len(a)):
        if(a[i]==0):
            j=i+1
            
            while(j<n and a[j]==0):
                j+=1
            
            if(j<n):
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
            else:
                break
    return a

if (__name__=="__main__"):
    
    print(moveZeroes([4,2,4,0,0,3,0,5,1,0]))
