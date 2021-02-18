def InsertionSort(a):

    for i in range (1, len(a)):

        j=i-1

        key= a[i]

        while (j>=0 and key < a[j]):

            a[j+1]= a[j]

            j-=1

        a[j+1]= key
    
    return a

def main():

    print(InsertionSort([4,3,2,5,10,1]))

if(__name__=="__main__"):
    main()

