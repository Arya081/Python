def count_upper_lower():
    n=input('enter string ')
    up=0
    low=0
    for char in n:
        if char.isupper():
            up=up+1
        else:
            low=low+1
    print('uppercase characters are ',up)
    print('lowercase characters are ',low)



count_upper_lower()




output
enter string ArYA
uppercase characters are  3
lowercase characters are  1
