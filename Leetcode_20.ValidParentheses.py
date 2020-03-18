def StrCheck(string):
    a=list(string)
    
    stc=list()
    
    i=0
    
    for i in range (0, len(a)):
        
        # print(a[i])
        
        if ( a[i]== "{" or a[i]== "(" or a[i]== "[" ):
            
            # print ("in")
            stc.append(a[i])
            
            top+=1
        
        else:
            
            if((a[i]=="}" and stc[top]== "{") or
               (a[i]==")" and stc[top]== "(") or
               (a[i]=="]" and stc[top]== "[") ):
                
                top-=1
            
            else:
                return False
    
    if(top==-1):
        return True
    else:
        return False
    
if (__name__=="__main__"):
    print(StrCheck("{[]}"))
    
    
