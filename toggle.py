def toggle(str):
    #str=input('enter string ')
    str1=''
    for i in range(len(str)):
        if(str[i]>='A' and str[i]<='Z'):
            str1=str1+chr((ord(str[i])+32))
        elif(str[i]>='a' and str[i]<='z'):
            str1=str1+chr((ord(str[i])-32))
        else:
            str1=str1+str[i]
    
    print('original string =',str)
    print('the given string after toggling case= ',str1 )

str=input('enter string ')
toggle(str)


output

enter string ArYA
original string = ArYA
the given string after toggling case=  aRya

=== Code Execution Successful ===
