def print_word(word):
    n = len(word)
    for i in range(n):
        for j in range(n):
            if i == j or i + j == n-1:
                print(word[i], end="")
            else:
                print(" ", end="")
        print()
    
# Test the function with an example word
word = "PRAABINDH"
print_word(word)

'''
Output

P       P
 R     R
  A   A
   A A
    B
   I I
  N   N  
 D     D
H       H
'''