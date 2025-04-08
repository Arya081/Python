f=open("IA2.txt","r")
#if os.path.isfile(name):
data=str(f.readlines())
print(data)
x=data.split()
print(x)
print(x.count("arya"))



output

['hello arya here.I arya is a student of pdeu']
["['hello", 'arya', 'here.I', 'arya', 'is', 'a', 'student', 'of', "pdeu']"]
2
