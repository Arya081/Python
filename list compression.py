def new():
    a=[32,100,50,90,66]
    b=[10,50,66,73,89]
    x=[n for n in a if n not in b]
    print(a)
    print(b)
    print('third list is ',x)

new()



output

[32, 100, 50, 90, 66]
[10, 50, 66, 73, 89]
third list is  [32, 100, 90]

=== Code Execution Successful ===
