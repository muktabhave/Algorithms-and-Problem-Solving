def reverse(s):
    return(s[::-1])

def IsPalindrome(no): 
    n= list(map(int, str(no)))
    
    rev= reverse(n)

    if (n==rev):

        return True

    else:
        return False

    return val
    

def main():
    print(IsPalindrome(101))

if (__name__=="__main__"):
    main()
