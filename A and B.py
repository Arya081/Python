name=['alice','anjali','bob','bobby','ben','bonny']
print(name)
a=set()
b=set()
for i in name:
    if i.startswith("a"):
        a.add(i)
    else:
        b.add(i)
print('set begning with a:',a)
print('set begning with b:',b)


output
['alice', 'anjali', 'bob', 'bobby', 'ben', 'bonny']
set begning with a: {'anjali', 'alice'}
set begning with b: {'bobby', 'ben', 'bob', 'bonny'}
