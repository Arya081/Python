class Complex:
    def config(self,r=0.0,i=0.0):
        self.real=r
        self.imag=i
    def add(self,other):
       z=Complex()
       z.real=self.real+other.real
       z.imag=self.imag+other.imag
       print(z.real, z.imag)
    def sub(self,other):
       z=Complex()
       z.real=self.real-other.real
       z.imag=self.imag-other.imag
       print(z.real, z.imag)
    def mul(self,other):
       z=Complex()
       z.real=self.real*other.real
       z.imag=self.imag*other.imag
       print(z.real, z.imag)
    def div(self,other):
       z=Complex()
       z.real=self.real/other.real
       z.imag=self.imag/other.imag
       print(z.real, z.imag)
    
c1=complex(1.1,0.2)
c2=complex(2.2,0.4)

print('addition is')
Complex.add(c1,c2)

print('substraction is')
Complex.sub(c1,c2)

print('multiplication is')
Complex.mul(c1,c2)

print('division is')
Complex.div(c1,c2)


output

addition is
3.3000000000000003 0.6000000000000001
substraction is
-1.1 -0.2
multiplication is
2.4200000000000004 0.08000000000000002
division is
0.5 0.5
>>> 

