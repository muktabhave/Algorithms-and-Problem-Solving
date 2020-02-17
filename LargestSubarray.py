def MaxSubarray(arr):
    maxsum= float('-inf')
    sum=0
    result=[]
    p=0
    
    
    for i in range (len(arr)):
        sum=sum+arr[i]
        
        if (sum> maxsum):
            maxsum=sum
            result=[p,i]
        if (sum<=0):
            p=i+1
            sum=0
    return result

if (__name__=='__main__'):
    
    print (MaxSubarray([-1, 2, 4, -3, 8]))
