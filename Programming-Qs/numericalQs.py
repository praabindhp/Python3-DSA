# Input: [2,1,0,-8,-9]
# Output: 0.4 , 0.2 , 0.4

# Explanation:
# First, find the total number of elements in the array = 5
# Find the total number of positive numbers=2
# Find the total number of neutral numbers=1
# (0 is the only neutral number)
# Find the total number of negative numbers=2
# Output = [ (no of positive number/length of the array), (no of neutral numbers/length of the array), (no of negative numbers/length of the array) ]
# [⅖, ⅕, ⅖]
# [0.4, 0.2, 0.4]

list_data =  [2,1,0,-8,-9]
result_data = []

count_positive = 0
count_neutral = 0
count_negative = 0
length_arr = len(list_data)

for val in list_data:
  if val>0:
    count_positive += 1
  elif val<0:
    count_negative += 1
  else:
      count_neutral += 1

result_data.append(count_positive/length_arr)
result_data.append(count_neutral/length_arr)
result_data.append(count_negative/length_arr)

print(result_data)