#factorial
def factorial(number):
    fact=1
    for i in range(1,number+1):
            fact*=i
    return fact
n=int(input("enter value of n"))
print(factorial(n))
