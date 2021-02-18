def Heapify(a,i,n):
    left=2*i+1
    right=2*i+2
    maxidx=i

    if(left<=n and a[maxidx]<a[left]):
        maxidx=left
    
    if(right<=n and a[maxidx]<a[right]):
        maxidx=right
    
    if(i!=maxidx):
        temp=a[i]
        a[i]= a[maxidx]
        a[maxidx]=temp

        Heapify(a, maxidx, n)

def HeapSort(a):
    n=len(a)-1
    Heapify(a,0,n)
    
    i=n
    
    while(i>=0):
        temp=a[0]
        a[0]=a[i]
        a[i]=temp
        
        Heapify(a, 0, i-1)
        
        i-=1
        
    print(a)

def main():
    HeapSort([50,40,30,2,10,5])

if(__name__=="__main__"):
    main()

