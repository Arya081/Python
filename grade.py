phy=eval(input("enter the marks of physics "))
bio=eval(input("enter the marks of biology "))
chem=eval(input("enter the marks of chemistry "))
name=input("Enter name")

avg=(phy+chem+bio)/3
if avg>=80:
    grade='O'

elif avg>=70 and avg<80:
    grade='A+'
    
elif avg>=60 and avg<70:
    grade='A'
    
elif avg>=55 and avg<60:
    grade='b+'

elif avg>=55 and avg<50:
    grade='B'

elif avg>=45 and avg<50:
    grade='C'

elif avg>=40 and avg<45:
    grade='P'

elif avg>=0 and avg<40:
    grade='F'

else:
    grade='NA'
    
    
print(name,"has scaored ",avg,"average marks and grade is",grade)



output

enter the marks of physics 78
enter the marks of biology 88
enter the marks of chemistry 90
Enter namexyz
xyz has scaored  85.33333333333333 average marks and grade is O
