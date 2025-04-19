def count_alpha_digits():
    s=0
    c=0
    for x in str:
        if x.isalpha():
            s=s+1
        elif x.isdigit():
            c=c+1
    print({"alphabets are":s,"digits are":c})

str=input('enter string: ')
count_alpha_digits()


output

enter string: arya is 18
{'alphabets are': 6, 'digits are': 2}

=== Code Execution Successful ===
