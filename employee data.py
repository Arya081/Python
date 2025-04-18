def stat (data): 
    sala={}
    for roll,info in data.items(): 
        dept=info['dept'] 
        salary=info['salary'] 
        if dept not in sala: 
            sala[dept]=[] 
            sala[dept].append(salary) 
        res={} 
        for dept,s in sala.items(): 
            res[dept]={'min':min(s),'max':max(s)} 
        return res 
data={101:{'dept': 'SAles', 'salary': 500},102:{'dept': 'logs', 'salary': 200},103:{'dept': 'logs', 'salary':540}} 
print (stat (data))


output

{'SAles': {'min': 500, 'max': 500}}

=== Code Execution Successful ===
