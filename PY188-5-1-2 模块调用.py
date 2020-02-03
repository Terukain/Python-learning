import random#或者 from random import *
a=random.choice([1,2,4,6,7])
b=random.randint(0,100)
c=random.random()
d=random.choice([1, 2, 3, 5, 8, 13]) #list
e=random.choice('hello') #字符串
f=random.choice(['hello', 'world']) #字符串组成的list
print(a,b,c)
print(d,e,f)

