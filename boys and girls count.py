boy=('bob','jey')
name=(boy,'pari','maya','tina')
b=0
g=0
for i in name:
    if isinstance(i, tuple):
        b=len(boy)
    else:
        g=g+1
print(boy)
print(name)
print('boys = ',b)
print('girls = ',g)



output

('bob', 'jey')
(('bob', 'jey'), 'pari', 'maya', 'tina')
boys =  2
girls =  3

=== Code Execution Successful ===
