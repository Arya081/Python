def avg(l, i=0, c=0, sum=0):
    if i==len(l):
        return sum/c
    else:
        return avg(l,i+1,c+1,sum+l[i])
    
print(avg([1,2,3]))


output
2.0

=== Code Execution Successful ===
