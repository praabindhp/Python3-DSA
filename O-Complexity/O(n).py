# Linear Complexity
# O(n)

def arrayMultiply2(arr):
    mod_arr = []
    
    for num in arr:
        mod_arr.append(num * 2)
        
    return mod_arr

testData = [5,2,7,8,9]
print(arrayMultiply2(testData))