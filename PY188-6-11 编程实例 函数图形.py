def tuxing(long=5,wide=5,pattern="*"):
    for i in range(long):
        for j in range(wide):
            print(pattern,end=" ")
        print()

tuxing()
tuxing(4,3)
tuxing(2,6,"!")

