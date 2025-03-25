def fac():
    n=eval(input('enter number '))
    a=1
    for i in range(1,n+1):
        a=a*i
    print('factorial of ',n,'is',a)
fac()


output
enter number 4
factorial of  4 is 24
