faculty=['dhavni','ravinder','balamurali','sophia','sonam']
x=len(faculty)
final=filter(lambda a: len(a)>8,faculty)
print(list(final))


output
['balamurali']
