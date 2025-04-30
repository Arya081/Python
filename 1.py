class comp:
    def __init__(self, real, img):
        self.real=real
        self.img=img
    def __add__(self, other):
        real_r=self.real+ other.real
        img_i=self.img+other.img
        return comp(real_r, img_i)
    def __sub__(self,other):
        real_r=self.real-other.real
        img_i=self.img-other.img
        return comp(real_r, img_i)
    def __mul__(self, other):
        real_r=self.real*other.real
        img_i=self.img*other.img
        return comp(real_r,img_i)
    
        
c1 = comp(1, 2)
c2 = comp(2, 9)
c3 = c1 + c2
c4= c1-c2
c5=c1*c2

print('addition is',c3.real, c3.img)
print('substraction is',c4.real, c4.img)
print('multiplication is',c5.real, c5.img)




output

addition is 3 11
substraction is -1 -7
multiplication is 2 18

=== Code Execution Successful ===
