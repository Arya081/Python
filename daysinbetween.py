from datetime import datetime
d1=(23,3,2025)
d2=(20,2,2025)
obj1=datetime(d1[2],d1[1],d1[0])
obj2=datetime(d2[2],d2[1],d2[0])
diff=abs((obj2-obj1).days)

print('number of days between',d1,'and',d2,'is :',diff,'days')


ouput
number of days between (23, 3, 2025) and (20, 2, 2025) is : 31 days

=== Code Execution Successful ===

