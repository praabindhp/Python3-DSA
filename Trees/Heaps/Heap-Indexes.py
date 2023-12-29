class Node:
    def __init__(self):
        self.heap = []
        
    @staticmethod
    def getLeftChildIndex(index):
        return (index * 2) + 1
    
    @staticmethod
    def getRightChildIndex(index):
        return (index * 2) + 2
    
    @staticmethod
    def getParentIndex(index):
        return (index - 1) // 2