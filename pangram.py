def ispangram(s,s2):
    alphabets=set('abcdefghijklmnopqrstuvwxyz')
    if (set(str.lower(s))>= alphabets):
        print(s,'is pangram')
    else:
        print(s,'is not pangram')
    if (set(str.lower(s2))>= alphabets):
        print(s2,'is pangram')
    else:
        print(s2,'is not pangram')
        
s='The quick brown fox jumps over the lazy dog'
s2='Crazy Fredrick bought many very exquisite opal jewel'
ispangram(s,s2)



output

The quick brown fox jumps over the lazy dog is pangram
Crazy Fredrick bought many very exquisite opal jewel is pangram

=== Code Execution Successful ===
