class Queue:
    def __init__(self):
        # Initialize an empty list to represent the queue
        self.items = []

    def enqueue(self, item):
        # Implement this function
        self.items.append(item)
        return

    def dequeue(self):
        # Implement this function
        removedItem = self.items[0]
        self.items.remove(removedItem)
        return removedItem

    def is_empty(self):
        # Implement this function
        if len(self.items) == 0:
            return True
        else:
            return False

    def size(self):
        # Implement this function
        return len(self.items)