def StrCheck(string):
    a=list(string)
    
    stc=['a', 'b']
    
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
    
