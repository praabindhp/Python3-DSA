# Quadratic Complexity
# O(n^2)
# Space Complexity
# O(n)

def nestedLoopCount(arr):
    result = []
    counter = 0
    
    for i in arr:
        for j in arr:
            counter += 1
            result.append(counter)
            print(counter)
            
    return result

testData = [1,2,3]
output = nestedLoopCount(testData)
print(output)