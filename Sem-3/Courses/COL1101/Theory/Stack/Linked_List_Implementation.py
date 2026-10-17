class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Stack:
    def __init__(self):
        self.top=None

    def push(self,value):
        new_node=Node(value)

        new_node.next=self.top
        self.top=new_node

    def pop(self):
        if self.top is None: return

        x=self.top.value
        self.top=self.top.next

        return x

    def peek(self):
        if self.top is None: return

        x=self.top.value
        return x

    def isempty(self):
        if self.top is None: return True
        return False
