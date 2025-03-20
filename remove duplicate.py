import random
l=[]
for i in range(50):
    n=random.randint(1,100)
    l.append(n)

print('original list',l)

s=set(l)

l=list(s)
print('new list',l)



output

original list [67, 81, 81, 22, 8, 79, 74, 65, 8, 100, 76, 91, 73, 4, 97, 81, 59, 81, 4, 81, 59, 40, 50, 28, 45, 66, 45, 65, 97, 6, 85, 76, 72, 20, 4, 42, 29, 47, 47, 43, 28, 78, 21, 90, 76, 83, 65, 33, 71, 36]
new list [4, 6, 8, 20, 21, 22, 28, 29, 33, 36, 40, 42, 43, 45, 47, 50, 59, 65, 66, 67, 71, 72, 73, 74, 76, 78, 79, 81, 83, 85, 90, 91, 97, 100]

=== Code Execution Successful ===




