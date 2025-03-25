s=set()
s.add("Arya")
s.add("Riya")
s.add("yesha")
s.add("kavya")
s.add("shana")
print(s)

s.update(["janya"])
print(s)
s.discard("shana")
s.remove("kavya")
print(s)


output

{'Riya', 'yesha', 'kavya', 'Arya', 'shana'}
{'Riya', 'yesha', 'janya', 'kavya', 'Arya', 'shana'}
{'Riya', 'yesha', 'janya', 'Arya'}
