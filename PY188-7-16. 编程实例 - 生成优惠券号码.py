import random
import string
a=list(string.ascii_letters)

for i in range(200):
    random.shuffle(a)
    b="".join(a)
    print(b[:8])

