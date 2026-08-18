# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.

Note that after backspacing an empty text, the text will continue empty.

 

Example 1:

Input: s = "ab#c", t = "ad#c"
Output: true
Explanation: Both s and t become "ac".
Example 2:

Input: s = "ab##", t = "c#d#"
Output: true
Explanation: Both s and t become "".
Example 3:

Input: s = "a#c", t = "b"
Output: false
Explanation: s becomes "c" while t becomes "b".
 

Constraints:

1 <= s.length, t.length <= 200
s and t only contain lowercase letters and '#' characters.
 

Follow up: Can you solve it in O(n) time and O(1) space?

ANS:


class Solution:
    def ComputedStr(self,str1):
        str1=list(str1)
        stc=[]
        i=0
        while(i< len(str1)):
            if(str1[i]=="#" and len(stc)>0):
                stc.pop()
            else:
                stc.append(str1[i])
            i+=1
        return stc
    
    def backspaceCompare(self, str1: str, str2: str) -> bool:

        stc1= self.ComputedStr(str1)
        stc2= self.ComputedStr(str2)

        if(stc1==stc2):
            return True
        else:
            return False    
