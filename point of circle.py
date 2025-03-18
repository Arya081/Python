def circle(x,y,rad,a,b):
    if((pow((a-x),2)+pow((b-y),2))<=pow(rad,2)):
        print("point lies inside")
    else:
        print(" point lies outside")

circle(0,0,2,3,1)



output

point lies outside
