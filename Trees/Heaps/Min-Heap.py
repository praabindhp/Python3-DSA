# Heaps
# Write a Python function that takes a list of integers and an integer k as input and returns the kth largest element in the list.

# Example:

# >>> nums = [3, 4, 1, 5, 9, 2, 6]
# >>> k = 3
# >>> find_kth_largest(nums, k)
 
# The largest 3 elements are 9, 6 and 5
# Since k = 3, the third largest element is 5

import heapq

def find_kth_largest(nums, k):
    # Implement this function
    minHeap = []
    
    for num in nums:
        heapq.heappush(minHeap, num)
        
        if len(minHeap) > k:
            heapq.heappop(minHeap)
        
    return minHeap[0]