# Constants In O()
# O(2n)

def loopTwice(arr):
    arrCopy1 = []
    arrCopy2 = []
    
    for i in arr:
        print(i)
        arrCopy1.append(i)
        
    for i in arr:
        print(i)
        arrCopy2.append(i)
        
testData = [1,2,3,4]
loopTwice(testData)
