l=eval(input("enter length of rectangle"))
b=eval(input("enter breath of rectangle"))

area=l*b
peri=2*(l+b)

if area>peri:
  print(" area",area,"greater than perimeter",peri)

else:
  print(peri," perimeter greater than area ",area)

  

output
enter length of rectangle20
enter breath of rectangle10
 area 200 greater than perimeter 60

