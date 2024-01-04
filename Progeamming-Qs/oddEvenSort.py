# arrange odd numbers in descending order and even numbers in ascending order
# [1,3,2,5,6,8,9,4]
# Output: []

# Define a function to sort odd and even numbers
def sort_odd_even(arr):
  # Create two empty lists for odd and even numbers
  odd = []
  even = []
  # Loop through the input array and append odd and even numbers to their respective lists
  for num in arr:
    if num % 2 == 0:
      even.append(num)
    else:
      odd.append(num)
  # Sort the odd list in descending order and the even list in ascending order
  odd.sort(reverse=True)
  even.sort()
  # Return the concatenation of the two lists
  return odd + even

# Test the function with an example array
arr = [1, 2, 3, 5, 4, 7, 10]
print(sort_odd_even(arr))