def compute():
    n=eval(input('enter number '))
    ans=1
    for i in range(0,4):
        ans=n**(i-2)+n**(i-1)+n**i
    
    print('addition is ',ans)



compute()

