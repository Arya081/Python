def convert(s):
    string=s.split()
    letter=sorted(list(set(string)))
    print(' '.join(letter))

s=input('enter string ')
print(convert(s))



output
enter string pdpu hello arya here
arya hello here pdpu
None

=== Code Execution Successful ===
