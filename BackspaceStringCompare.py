# Given two strings S and T, return if they are equal when both are typed into empty text editors. # means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

def BackspaceStringCompare(c1,c2):
    c1=list(c1)
    c2=list(c2)
    stc1=[]
    stc2=[]
    
    i=0
    while(i< len(c1)):
        if(c1[i]=="#" and len(stc1)>0):
            stc1.pop()
        else:
            stc1.append(c1[i])
        i+=1
    j=0
    while(j<len(c2)):
        if(c2[j]=="#" and len(stc2)>0):
            stc2.pop()
        else:
            stc2.append(c2[j])
        j+=1        
    
    if(stc1==stc2):
        return True
    else:
        return False    
    
    
if(__name__=="__main__"):
    print(BackspaceStringCompare('ab#d','aec##d'))
