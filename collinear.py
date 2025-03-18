def collinear(a,b,x,y,p,q):
    slope=a*(y-q)+x*(q-b)+p*(b-y)
    if(slope==0):
        print(" it is collinear")
    else:
        print(" it is not collinear")

collinear(1,1,1,8,4,5)




output


it is not collinear
