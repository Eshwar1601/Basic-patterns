#primenumber
def is_prime(number):
    if number>1:
        for i in range(2,int(n**0.5)+1):
            if n%i ==0 and i!=n:
                return False
        return True

n=int(input("enter number"))
print("prime" if is_prime(n) else "not prime")