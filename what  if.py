print("number comparison")
a = int(input("enter first namber a  "))
b = int(input("enter second namber b  "))
c = int(input("enter third namber c  "))
if a > b:
    print(":) a > b")

elif a == b:
    if c > b:
        print(":) c > b")
    else:
        print(":( c < b")
else:
    print(":( a < b")