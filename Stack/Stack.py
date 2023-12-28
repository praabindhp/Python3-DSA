class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        
    def push(self, value):
        newNode = Node(value)
        newNode = self.top
        self.top = newNode
    
    def pop(self):
        if not self.isEmpty():
            poppedItem = self.top.value
            self.top = self.top.next
            return poppedItem
    
    def isEmpty(self):
        return self.top is None