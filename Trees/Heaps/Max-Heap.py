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
    
class MaxHeap:
    def __init__(self) -> None:
        pass
    
    def _heapify_up(self):
        currentIndex = len(self.heap) - 1
        while currentIndex > 0:
            parentIndex = self.getParentIndex(currentIndex)
            if self.heap[currentIndex] > self.heap[parentIndex]:
                # Swap Function
                self.heap[currentIndex], self.heap[parentIndex] = self.heap[parentIndex], self.heap[currentIndex]
            else:
                break
            currentIndex = parentIndex
            
    def _heapify_down(self):
        currentIndex = 0
        while self.getLeftChildIndex(currentIndex) < len(self.heap):
            leftChildIndex = self.getLeftChildIndex(currentIndex)
            rightChildIndex = self.getRightChildIndex(currentIndex)
            
            if rightChildIndex < len(self.heap):
                if self.heap[leftChildIndex] > self.heap[rightChildIndex]:
                    index = leftChildIndex
                else:
                    index = rightChildIndex
            else:
                index = leftChildIndex
                
            if self.heap[currentIndex] < self.heap[index]:
                # Swap Function
                self.heap[currentIndex], self.heap[index] = self.heap[index], self.heap[currentIndex]
            else:
                break
            currentIndex = index
    
    def insert(self, value):
        self.heap.append(value)
        self._heapify_up()
        
    def pop(self):
        if len(self.heap) == 0:
            return None
        
        if len(self.heap) == 1:
            return self.heap.pop()
        
        maxValue = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down()
        
        return maxValue