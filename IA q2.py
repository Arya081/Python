def pattern(n):
    for i in range(n,n-1,-1):
        for j in range(n,0,-1):
            print("*"*j)

pattern(3)




output

***
**
*
