import random

def game(num):
    a=int(input("What I think:"))
    if a>num:
        print("Too big!")
        #return False
    if a<num:
        print("Too small!")
        #return False
    else:
        print("bingo!")
        return True

def play():
    num=random.randint(1,10)
    while not game(num):
           pass
    ##while True: 另一种写法
       #if game(num):
            #break
while True:
    choice=int(input("1.Play game;2.Exit"))
    if choice==1:
        play()
    if choice==2:
        break
    
