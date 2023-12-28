s = "(())"

def is_balanced(s):
    bracketStack = []
    for b in s:
        if b == '(':
            bracketStack.append(b)
        if b == ')':
            bracketStack.pop()
    
    if len(bracketStack) == 0:
        return True
    else:
        return False
    
print(is_balanced(s))