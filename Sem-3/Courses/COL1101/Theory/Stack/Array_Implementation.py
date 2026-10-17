class Stack:
    def __init__(self,capacity):
        self.arr=[None]*capacity
        self.capacity=capacity
        self.top=-1           # Maintains the index of top-most element

    "Inserts a value at the top"
    def push(self,value):
        if self.top==self.capacity-1:
            return

        self.top+=1
        self.arr[self.top]=value

    "Returns the value at the top"
    def peek(self):
        if self.top==-1: return 

        return self.arr[self.top]

    "Removes the top most element"
    def pop(self):
        if self.top==-1: return
        
        x=self.arr[self.top]
        self.arr[self.top]=None

        self.top-=1
        return x

    def isempty(self):
        if self.top==-1: return True
        return False
    

    # Below are only useful for dynamic size array
    def resize(self):
        self.capacity*=2

        new_stack=[None]*self.capacity
        for i in range(self.top+1):new_stack[i]=self.stack[i]

        self.stack=new_stack

    def shrink(self):
        if self.capacity>2 and self.top+1<=self.capacity//4:
            self.capacity//=2

            new_stack=[None]*self.capacity

            for i in range(self.top+1): new_stack[i]=self.stack[i]
            self.stack=new_stack
