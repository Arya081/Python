import random
odd=[]
even=[]
for i in range(5):
    n=random.randrange(1,100,2)
    odd.append(n)
print(odd)


for i in range(5):
    x=random.randrange(2,100,2)
    even.append(x)
print(even)

odd[2]=even
print(odd)

flatten=[]
for x in odd:
    if isinstance(x, list):
        flatten.extend(x)
    else:
        flatten.append(x)
print(flatten)

print(flatten.sort())



output
[63, 51, 91, 47, 41]
[10, 14, 54, 92, 6]
[63, 51, [10, 14, 54, 92, 6], 47, 41]
[63, 51, 10, 14, 54, 92, 6, 47, 41]
None

=== Code Execution Successful ===




