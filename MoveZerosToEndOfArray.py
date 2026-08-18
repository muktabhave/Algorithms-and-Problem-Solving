Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]
 

Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1
 

Follow up: Could you minimize the total number of operations done?
 
ANS:

def moveZeroes(a):
    n=len(a)
    j=0
    for i in range(len(a)):
        if(a[i]==0):
            j=i+1
            
            while(j<n and a[j]==0):
                j+=1
            
            if(j<n):
                tmp=a[i]
                a[i]=a[j]
                a[j]=tmp
            else:
                break
    return a

if (__name__=="__main__"):
    
    print(moveZeroes([4,2,4,0,0,3,0,5,1,0]))
