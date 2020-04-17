# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# push(x) -- Push element x onto stack.
# pop() -- Removes the element on top of the stack.
# top() -- Get the top element.
# getMin() -- Retrieve the minimum element in the stack.

class MinStack:

    def __init__(self):
        self.topele=-1
        self.min=-1
        self.items=[]
        
        
    def push(self, x: int) -> None:
        
        self.items.append(x)
        self.topele+=1
        if(self.topele==0):
            self.min=x
        else:
            if(x<self.min):
                self.min=x
        

    def pop(self) -> None:
        if(self.topele==-1):
            return
        if(self.min==self.items[self.topele]):
            self.min=self.items[0]
            for j in range (0,self.topele):
                if (self.items[j]<self.min):
                    self.min= self.items[j]
            
        
        self.items.pop()
        self.topele-=1
        

    def top(self) -> int:
        return self.items[self.topele]    
    
    def getMin(self) -> int:
        return self.min
