def twoSum(nums, target):
         
    n=len(nums)
        
    for j in range(n-1):
        
        key= nums[j]
        i=j+1

        for i in range (n):
                
            if ((key+ nums[i])== target):
                    
                a= [i, j]
                return a
def main():

    print(twoSum([7,2,11,5], 16))

if (__name__=="__main__"):
    main()
