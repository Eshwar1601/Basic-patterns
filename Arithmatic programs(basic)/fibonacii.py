#fibaonacii
n=int(input("enter n"))
a,b=0,1
for _ in range(n):
    print(a,end=" ")
    a,b=b,a+b