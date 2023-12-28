class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self) -> None:
        self.front = None
        self.back = None
        self.size = 0
    
    def isEmpty(self):
        return self.size == 0
    
    # O(1)
    def enqueue(self, value):
        newNode = Node(value)
        if self.isEmpty():
            self.back = newNode
            self.front = newNode
        else:
            newNode.next = self.back
            self.back = newNode
        self.size += 1
    
    # O(1)
    def dequeue(self):
        if not self.isEmpty():
            removedNode = self.front
            self.front = removedNode.next
            self.size -= 1
            if self.isEmpty():
                self.back = None
            return removedNode.value
        else:
            print("Queue Is Empty")