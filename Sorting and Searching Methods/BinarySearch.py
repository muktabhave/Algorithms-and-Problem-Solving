#import math
def BinarySearch (a, s):

    l=0;
    r=len(a)-1

    while (l<r):

        mid=l+r/2

        if(s==a[mid]):
            return mid

        elif (s< a[mid]):
            r=mid-1
        else:
            l=mid+1
    return "Not Found"

def main():

    print (BinarySearch([1,2,3,5,6], 2))

if (__name__=="__main__"):
    main()

