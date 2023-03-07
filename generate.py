import random

a = int(input("enter the number of generated numbers  "))

i=0
while i<a:
    d = random.randint(0,9)
    print(d)
    i = i+1