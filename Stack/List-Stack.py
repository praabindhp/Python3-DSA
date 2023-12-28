myStack = []

def push(myStack, x):
    myStack.append(x)
    
def pop(myStack):
    if len(myStack) > 0:
        poppedItem = myStack.pop()
        return poppedItem
    
push(myStack, 32)
push(myStack, 36)
push(myStack, 38)
print(myStack)
print(myStack.pop())
print(myStack)