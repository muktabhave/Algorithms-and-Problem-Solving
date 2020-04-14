class MinStack:

    def __init__(self):
        top=-1
        min=-1
        

    def push(self, x: int) -> None:
        self.append(x)
        top=top+1
        min=getMin(self)

    def pop(self) -> None:
        self.pop()
        top=top-1
        min=getMin(self)

    def top(self) -> int:
        return top

    def getMin(self) -> int:
        if(top==-1):
            return "Stack is empty"
        elif (top==0):
            min=
