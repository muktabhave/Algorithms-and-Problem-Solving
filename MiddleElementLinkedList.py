# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

class Node:
    
    def __init__(self,data):
        self.data=data
        self.next=None
    
class LinkedList:
    
    def __init__(self):
        self.head= None

    def pushll(self,ele):
        #if LL is empty
        if(self.head== None):
            self.head= Node(ele)
        
        else:
            tmp= self.head
            
            while(tmp.next!=None):
                tmp=tmp.next
            
            tmp.next=Node(ele)
    
    def FindMiddleEle(self):
        
        if(self.head== None):
            print ("List is empty")
        
        else:
            
            count=0
            i=self.head
            
            while(i.next!=None):
                count+=1
                i=i.next
            
            mid=(count+1)/2
            
            i=self.head
            
            j=0
            while(j<=mid-1):
                prev=i
                i=i.next
                j+=1
            if(count%2==0):
                print (i.data)
            else:
                print (prev.data,i.data)
        
    def printll(self):
        
        if(self.head== None):
            print("List is empty")
        else:
            tmp=self.head
            while(tmp!=None):
                print(tmp.data)
                tmp=tmp.next

if __name__=="__main__":
    ll= LinkedList()
    ll.pushll(10)
    ll.pushll(20)
    ll.pushll(30)
    # ll.pushll(40)
    
    ll.printll()
    
    ll.FindMiddleEle()
            
