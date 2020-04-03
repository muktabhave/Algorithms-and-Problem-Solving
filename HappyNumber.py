class Solution:
    def isHappy(self, num: int) -> bool:

        while(1):

            l= list(map(int, str(num)))
            sum=0
            for i in range (len(l)):
                sum=sum+(l[i]*l[i])
            num=sum

            if(num==1):
                return 1
            elif(num==4):
                return 0
