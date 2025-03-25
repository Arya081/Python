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
Number of elements less than 30 are:  5
