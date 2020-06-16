/* Given a 32-bit signed integer, reverse digits of an integer. 

Trick is how you convert number to list and list back to number
*/

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

        
