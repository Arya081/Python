def remove(str):
    a=input('enter string to be removed: ')
    x=[a]
    for i in x:
        str=str.replace(i,'')
        print(str)
    
    
str=input('enter string: ')
remove(str)


output

enter string: welcome in pdeu
enter string to be removed: in pdeu
welcome 

=== Code Execution Successful ===
