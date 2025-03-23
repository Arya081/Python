tup=('arya',5,'p')
print(tup)
l=list(tup)
l[0]='ap'
l.pop(0)
tup=tuple(l)
print(tup)


output

('arya', 5, 'p')
(5, 'p')

=== Code Execution Successful ===
