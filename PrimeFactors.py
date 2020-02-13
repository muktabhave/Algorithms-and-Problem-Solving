def PrimeFactors(n):
    
    if (n==0):
        print("Number is 0")
    
    else:
        if(n%2==0):
            print("2*")
            if(n/2==1):
                return
            else:
                PrimeFactors(n/2)
        
        elif(n%3==0):
            print("3*")
            if(n/3==1):
                print(1)
            else:
                PrimeFactors(n/3)
        
        elif(n%5==0):
            print("5*")
            if(n/5==1):
                print(1)
            else:
                PrimeFactors(n/5)
        
        elif(n%7==0):
            print("7*")
            if(n/7==1):
                print(1)
            else:
                PrimeFactors(n/7)
        
        else:
            print(n,"*")
            print(1)
            
if(__name__=="__main__"):
    
    PrimeFactors(1001)
