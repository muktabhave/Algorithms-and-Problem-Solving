def HappyNumber(num):

    while(len(list(map(int, str(num))))>1):
        l= list(map(int, str(num)))
        sum=0
        for i in range (len(l)):
            sum=sum+(l[i]*l[i])
        num=sum
    # print (num)
    if(num==1):
        return 1
    else:
        return 0

if (__name__=="__main__"):
    print(HappyNumber(68))
