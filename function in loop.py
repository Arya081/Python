def fun():
    print('function called')
def disp():
    print('Disp called')
def msg():
    print('MSg called')
    
function=[fun,disp,msg]

for f in function:
    f()


output

function called
Disp called
MSg called
