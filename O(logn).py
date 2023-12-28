# Logarithmic Complexity
# O(log n)

# Binary Search

# Recursion
def binary_search_recursive(arr, low, high, target):

  if low > high:
    return -1

  mid = (low + high) // 2
  mid_element = arr[mid]
  
  if mid_element == target:
    return mid

  elif mid_element > target:
    return binary_search_recursive(arr, low, mid - 1, target)

  else:
    return binary_search_recursive(arr, mid + 1, high, target)

# Iterative approach
def binary_search_iterative(arr, target):
    
  low = 0
  high = len(arr) - 1

  while low <= high:

    mid = (low + high) // 2
    mid_element = arr[mid]

    if mid_element == target:
      return mid
    elif mid_element > target:
      high = mid - 1
    else:
      low = mid + 1
      
  return -1

# Built-in bisect module
import bisect
def binary_search_bisect(arr, target):
    
  i = bisect.bisect_left(arr, target)
 
  if i < len(arr) and arr[i] == target:
    return i

  return -1