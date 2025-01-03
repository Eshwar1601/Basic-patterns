#Right-Angled Triangle of Stars
n=int(input("enter n value"))
for i in range(1,n):
    for j in range(i):
        print("*",end="")
    print()