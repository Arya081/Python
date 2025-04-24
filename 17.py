def replace(l, x=0):
    if x==len(l):
        return l
    elif l[x]<0:
        l[x]=0
        return replace(l, x+1)
    else:
        return replace(l, x+1)

ans=replace([-2,-5,-3,9,1,2,0,4,5])
print("Updated list is:",ans)



output

Updated list is: [0, 0, 0, 9, 1, 2, 0, 4, 5]

=== Code Execution Successful ===
