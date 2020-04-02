def GetKey(val, a):
    
    for key,value in a.items():
        if(val==value):
            return key
        
def SingleNumber(l):
    
    nums= dict()
    
    for i in l:
        if(l[i] in nums):
            
            nums[l[i]]=2
        
        else:
            
            nums[l[i]]=1
    print(nums)

    return GetKey(1, nums)


if (__name__=="__main__"):
    
    print (SingleNumber([2,2,1]))
    
    
