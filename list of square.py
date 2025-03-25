import random
l=[random.randint(-15,15) for i in range(11)]
print('list of random number is',l)
x=map(lambda a: a**2,l)
print('square list',list(x))


output

list of random number is [4, 14, 15, -12, -7, 10, -6, 9, -1, 8, 1]
square list [16, 196, 225, 144, 49, 100, 36, 81, 1, 64, 1]
