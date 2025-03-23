tup=(1,2,3)
l=list(tup)
l[1]=3

print('original tuple',tup)
tup=tuple(l)
print('modified tuple',tup)


output

original tuple (1, 2, 3)
modified tuple (1, 3, 3)

=== Code Execution Successful ===
