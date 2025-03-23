import random
l=[]
for i in range(30):
    n=random.randint(-50,50)
    l.append(n)

print(l)

pos=[]
neg=[]
for x in l:
    if x>0:
        pos.append(x)
    else:
        neg.append(x)
print('List of Positive number is ',pos)
print('List of negative number is ',neg)



output

[-5, 32, -5, -43, -11, 19, -22, -23, 48, 23, 25, -21, 22, -40, -3, -15, 35, -16, -46, 47, -37, -9, -25, 3, 26, 19, 25, 23, 39, 37]
List of Positive number is  [32, 19, 48, 23, 25, 22, 35, 47, 3, 26, 19, 25, 23, 39, 37]
List of negative number is  [-5, -5, -43, -11, -22, -23, -21, -40, -3, -15, -16, -46, -37, -9, -25]

=== Code Execution Successful ===
