a=eval(input("enter 1st value"))
b=eval(input("enter 2nd value"))
c=eval(input("enter 3rd value"))
if a>b and a>c:
  print("largest is",a)
elif b>a and b>c:
    print("largest is",b)
    
else:
  print("largest is",c)

  
if a<b and a<c:
  print("smallest is",a)
elif b<a and b<c:
    print("smallest  is",b)
    
else:
  print("smallest  is",c)
  



output

enter 1st value45
enter 2nd value55
enter 3rd value67
largest is 67
smallest is 45
