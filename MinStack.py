# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class Stack:

    def __init__(self):
        self.top=-1
        self.min=-1
        self.items=[]
        
        
    def push(self, x: int) -> None:
        
        self.items.append(x)
        self.top+=1
        if(self.top==0):
            self.min=x
        else:
            if(x<self.min):
                self.min=x
        

    def pop(self) -> None:
        if(self.min==self.items[self.top]):
            self.min=self.items[0]
            for j in range (1,self.top-1):
                if (self.items[j]<self.min):
                    self.min= self.items[j]
            
        
        self.items.pop()
        self.top-=1
        

    def top(self) -> int:
        return self.top    
    
    def getMin(self) -> int:
        return self.min
            
    
if (__name__=="__main__"):
    
    s=Stack()
    
    s.push(10)
    s.push(5)
    s.push(20)
    s.push(30)
    s.pop()
    s.pop()
    s.pop()
    print (s.items)
    print(s.getMin())
