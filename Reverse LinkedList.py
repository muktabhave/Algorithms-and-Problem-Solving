class Node:

    def __init__(self, data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=None

    def ReverseLL(self):
        tmp= self.head
        next= self.head
        while(next!=None):
            prev=tmp
            tmp=tmp.next
            next=tmp.next.next
            tmp.next=prev
            if(prev==self.head):
                prev.next=None
            if(next==None):
                self.head=tmp
            tmp.next=prev
        
        return self
    
    def pushll(self,ele):
        #if LL is empty
        if(self.head== None):
            self.head= Node(ele)
        
        else:
            tmp= self.head
            
            while(tmp.next!=None):
                tmp=tmp.next
            
            tmp.next=Node(ele)
    
    def printll(self):
        
        if(self.head== None):
            print("List is empty")
        else:
            tmp=self.head
            while(tmp!=None):
                print(tmp.data)
                tmp=tmp.next
    
if (__name__=="__main__"):
    ll= LinkedList()
    ll.pushll(10)
    ll.pushll(20)
    ll.pushll(30)
    ll.printll()
    
    ll.ReverseLL()
    
    ll.printll()
