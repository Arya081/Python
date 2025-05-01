def fun(l):
    for n in l:
        s=set(n.upper())
        print(s)
        
fun(['arya'])


output
{'R', 'A', 'Y'}
>>> 




l=['arya','in','pdeu']
new=list(map(str.upper,l))

s=set(new)
print(s)


output
{'IN', 'ARYA', 'PDEU'}

=== Code Execution Successful ===
