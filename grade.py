
phy=eval(input("enter the marks of physics "))
bio=eval(input("enter the marks of biology "))
chem=eval(input("enter the marks of chemistry "))

avg=(phy+chem+bio)/3
if avg>=80:
    grade='Distinction'

elif avg>=60 and avg<80:
    grade='first division'
    
elif avg>=45 and avg<60:
    grade='second division'
    
elif avg>=40 and avg<45:
    grade='pass'
    
else:
    grade='promotiion not granted'
    
    
print(grade)






output

enter the marks of physics 50
enter the marks of biology 80
enter the marks of chemistry 77
first division

=== Code Execution Successful ===
