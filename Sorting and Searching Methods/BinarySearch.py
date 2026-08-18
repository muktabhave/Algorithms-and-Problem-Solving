#import math

Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums. If target exists, then return its index. Otherwise, return -1.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
 

Constraints:

1 <= nums.length <= 104
-104 < nums[i], target < 104
All the integers in nums are unique.
nums is sorted in ascending order.

ANS:
    
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

