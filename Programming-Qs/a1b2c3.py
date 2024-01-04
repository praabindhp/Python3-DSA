# Input: a1b2c3
# Output: abbccc
# Caution: Don't use inbuilt functions

# Explanation:

# After we have the number 1 so a repeats one time = a
# After b we have the number 2 so it repeats two times = bb
# After c we have the number 3 so it repeats three times = ccc
# Final Output: abbccc

inString = "a1b2c3"
outString = ""

for i in range(0, len(inString), 2):
    outString += inString[i] * int(inString[i+1])
            
print(outString)