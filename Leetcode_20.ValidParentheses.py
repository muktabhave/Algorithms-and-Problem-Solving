Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.

ANS:

def StrCheck(string):
    a=list(string)
    
    stc=[]
    
    i=0
    
    for i in range (0, len(a)):
        
        # print(a[i])
        
        if ( a[i]== "{" or a[i]== "(" or a[i]== "[" ):
            
            # print ("in")
                        
            stc.append(a[i])
        
        else:
            
            if((a[i]=="}" and stc.pop()== "{") or
               (a[i]==")" and stc.pop()== "(") or
               (a[i]=="]" and stc.pop()== "[") ):
                
                if (len(stc)>0):
                    stc.pop()
                
            else:
                return False
    
    if(len(stc)==0):
        return True
    else:
        return False
    
if (__name__=="__main__"):
    print(StrCheck("{}[()]"))
    
