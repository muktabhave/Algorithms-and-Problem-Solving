def fibonacci_evensum(n):
    c=0
    i=1
    sum=0
    
    while(i<n):
        res=c+i
        c=i
        i=res
        if(res%2==0):
            sum=sum+res
    return sum

if (__name__=="__main__"):
    print(fibonacci_evensum(1000000))
