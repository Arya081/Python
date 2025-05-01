lst=['madam','Python','malayalam',12321]
for i in lst:
    if str(i)==(str(i)[::-1]):
        print(i)


output

madam
malayalam
12321


import random
n=['madam','python','malyalam','12321' ]
print(n)
l=list(filter(lambda i:str(i)==str(i)[::-1],n))
print(l)

output

['madam', 'python', 'malyalam', '12321']
['madam', '12321']

=== Code Execution Successful ===
