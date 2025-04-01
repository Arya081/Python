str=input("enter string ")
f=open("exercise.txt","wt",encoding="utf8")
f.write(str)
f.close()
f=open("exercise.txt","r")
print(f.read())




output

enter string how areyou
how areyou
>>> 
