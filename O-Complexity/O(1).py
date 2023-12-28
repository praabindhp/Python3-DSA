# Constant Complexity
# O(1)

def getFirstElement(arr):
    if len(arr) > 0:
        return arr[0]
    else:
        return None
    
testData = [5,2,7,8,9]
print(getFirstElement(testData))