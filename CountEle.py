
# Given an integer array arr, count element x such that x + 1 is also in arr.

# If there're duplicates in arr, count them seperately.

def CountEle(a):
    nums=dict()
    count=0
    
    for i in range (len(a)):
        nums.update({a[i]:a[i]})

    for j in range(len(a)):
        if((a[j]+1) in nums):
            count=count+1
            
    return count    
        
if(__name__=="__main__"):
    
    print(CountEle([1,3,2,3,5,0]))
