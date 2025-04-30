class  cal:
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def __mul__(self):
        area=self.l*self.b
        print(area)
    def peri(self):
        p=2*(self.l+self.b)
        print(p)
   
    
area=cal(2,4)
p=cal(2,4)
cal.__mul__(area)
cal.peri(p)


output

8
12

=== Code Execution Successful ===
