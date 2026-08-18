/* Given a 32-bit signed integer, reverse digits of an integer. 

Trick is how you convert number to list and list back to number
*/

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1

ANS:

class Solution:
    def reverse(self, x: int) -> int:
      
      if (x<0):
        sign= -1 
      else:
        sign=1
        
      l=list(map(int, str(abs(x))))
    
        
      start=0
      end=len(l)-1
    
        
      while (start<end):
        temp=l[start]
        l[start]= l[end]
        l[end]= temp
        start+=1
        end-=1
        
      res = int("".join(map(str, l)))
      
      if (res< (-2**31) or res> (2**31-1)):
        return 0
      else:
        
        return (sign*res)

        
