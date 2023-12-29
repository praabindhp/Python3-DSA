def two_sum(nums, target):
  hash_table = {}
  
  for i, num in enumerate(nums):
    
    if target - num in hash_table:
      return [hash_table[target - num], i]
    
    hash_table[num] = i

print(two_sum([2,7,11,15], 9))