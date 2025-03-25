lst=['madam','Python','malayalam',12321]
for i in lst:
    if str(i)==(str(i)[::-1]):
        print(i)


output

madam
malayalam
12321
