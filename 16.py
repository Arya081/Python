def power(a,b):
    if b==0:
        return 1
    return a * power(a,b-1)

n=float(input("Enter a number: "))
rais_to=int(input("Enter the power to which you want to find the value: "))
print(f"Value of given number is {power(n,rais_to)}")


output

Enter a number: 4
Enter the power to which you want to find the value: 2
Value of given number is 16.0

=== Code Execution Successful ===
