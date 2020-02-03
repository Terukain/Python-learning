from random import randint
num=randint(1,100)
print("Guess what I think?")
import time

b=False
print("please input number:")
while b==False:
    a=int(input())
    if a<num:
        print("Too small!")
        print("please input number:")
    if a>num:
        print("Too big!")
        print("please input number:")
    if a==num:
        print("Bingo!")
        b==True
