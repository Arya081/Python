def len_str(s):
    if s=="":  
        return 0
    else:
        return 1+len_str(s[1:])  

print(len_str("Github"))


output

6

=== Code Execution Successful ===
