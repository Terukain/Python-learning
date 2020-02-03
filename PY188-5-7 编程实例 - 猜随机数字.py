from random import randint
print("Guess what I think?")
import time
total=0
times=0
while True:
    option=int(input("1.Start Game?;or 2.End?\n"))
    if option==2:
        break
    if option==1:
        total+=1
        num=randint(1,100)
        while True:
            times+=1                      
            a=int(input("please input number:"))
            if a<num:
                print("Too small!")
            if a>num:
                print("Too big!")
            if a==num:
                print("Bingo")
                break
    else:
        break
if times>0:
    print("Total games:%d,Success rate:%f"%(total,float(times/total)))
print("Game Over.")
