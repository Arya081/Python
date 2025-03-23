from operator import itemgetter
l=[('samosa',80),('pasta',500),('pizza',150)]
tp=tuple(l)
print(tp)
tp2=sorted(tp,key=itemgetter(1))
print(tp2)


output

(('samosa', 80), ('pasta', 500), ('pizza', 150))
[('samosa', 80), ('pizza', 150), ('pasta', 500)]

=== Code Execution Successful ===
