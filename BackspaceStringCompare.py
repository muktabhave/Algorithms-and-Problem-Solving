# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

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
