def SelectionSort (a):

    for i in range (len(a)-1):

        min_idx= i

        j= i+1

        while j< len(a):

                if (a[j]< a[min_idx]):

                    min_idx=j
                
                j+=1
        
        if(i!=min_idx):
            temp= a[i]
            a[i]= a[min_idx]
            a[min_idx]= temp

    return a

print (SelectionSort([5,2,1,10,4,7]))
