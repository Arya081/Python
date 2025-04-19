def frequency():
    c={}
    str=s.lower().split()
    for x in s:
        c[x]=c.get(x,0)+1
    sort=sorted(c.items())
    print(sort)
    
s=input('enter string ')
frequency()


output

enter string welcome to pdpu
[(' ', 2), ('c', 1), ('d', 1), ('e', 2), ('l', 1), ('m', 1), ('o', 2), ('p', 2), ('t', 1), ('u', 1), ('w', 1)]

=== Code Execution Successful ===
