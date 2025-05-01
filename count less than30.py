import random
def fun(n):
    print(n)
    a=0
    for i in n:
        if i<30:
            a=a+1
        
    print("Number of elements less than 30 are: ",a)

n={random.randint(15,45) for i in range(10)}
        
fun(n)



output

{32, 34, 37, 41, 17, 21, 22, 26, 29}





import random
n={random.randint(15,45) for i in range (10)}
print(n)
c=0
for x in n:
    if x<30:
        c=c+1
print('numbers less than 30 are',c)

new=set(filter(lambda x:x<35,n))
print('set having less than 35:',new)


output

{35, 36, 37, 39, 45, 15, 17, 28}
numbers less than 30 are 3
set having less than 35: {17, 28, 15}

=== Code Execution Successful ===
