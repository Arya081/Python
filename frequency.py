
data=input('enter string')
freq={}
print(data)

for x in data:
    if x in freq:
        freq[x]=freq[x]+1
    else:
        freq[x]=1
    
print(freq)



output

enter string arya
arya
{'a': 2, 'r': 1, 'y': 1}

=== Code Execution Successful === 




