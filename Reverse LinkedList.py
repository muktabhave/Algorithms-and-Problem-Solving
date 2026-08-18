Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
 

Constraints:

The number of nodes in the list is the range [0, 5000].
-5000 <= Node.val <= 5000
 

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

ANS:

class Node:

    def __init__(self, data):
        self.data=data
        self.next=None


class LinkedList:
    def __init__(self):
        self.head=None

    def ReverseLL(self):
        tmp= self.head
        next=self.head.next
        
        while(next!=None):
            prev=tmp
            tmp=next
            next=next.next
            
            tmp.next=prev
            if(prev==self.head):
                prev.next=None
            
        self.head=tmp
                
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
    ll.pushll(40)
    
    ll.ReverseLL()
    
    ll.printll()
