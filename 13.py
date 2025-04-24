
def deci_to_bin(n):
    if n == 0:
        return ""  
    return deci_to_bin(n// 2) + str(n % 2)

print(deci_to_bin(178))



output

10110010

=== Code Execution Successful ===
