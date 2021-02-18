import math
def MergeSort(a):
    
    if (len(a)>1):
        m=math.floor(len(a)/2)
    
        X= a[:m]
        Y= a[m:]

        MergeSort(X)
        MergeSort(Y)

        i=0
        j=0
        k=0
        while(i<len(X) and j<len(Y)):
            if(X[i]< Y[j]):
                a[k]= X[i]
                i+=1
            else:
                a[k]= Y[j]
                j+=1
            k+=1 
        while(i<len(X)):
            a[k]= X[i]
            i+=1
            k+=1
        while(j<len(Y)):
            a[k]= Y[j]
            j+=1
            k+=1

        return a

def main():

    print(MergeSort([3,8,2,5,10]))

if( __name__=="__main__"):

    main()

 


