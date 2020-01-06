#Array rotation by storing into a temp Array

def ArrayRotate(no, a):

    tem=[]

    for i in range(no):

        tem.append(a[i])

        ar= len(a)-no

    for i in range(ar):

        a[i]= a[i+2]
    
    for i in range(no):

        a[ar+i]= tem[i]

    return (a)

def main():

    print (ArrayRotate(2, [3,4,5,6,7]))

if (__name__=="__main__"):
    main()

