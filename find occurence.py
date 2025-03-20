import random
l=[]
for i in range(20):
    n=random.randint(1,100)
    l.append(n)

print(l)

num=eval(input("enter the number to find its occurence"))

index=[i for i,x in enumerate(l) if x==num]
print(index)





output

[38, 99, 91, 96, 50, 10, 71, 26, 52, 19, 15, 79, 34, 17, 97, 15, 61, 44, 33, 41]
enter the number to find its occurence15
[10, 15]

=== Code Execution Successful ===
