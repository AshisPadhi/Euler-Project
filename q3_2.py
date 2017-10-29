def prime(n):
    for x in range(2,int(n**0.5)+1):
        if n%x == 0:
            return False
    return True

def factor(n,x):
    if n%x==0:
        return True
    return False

def largePrimeFactor(n):
    d=2
    highest = 0
    for x in range(2,n+1):
        if factor(n,x) and prime(x):
            highest=x
    return highest
print(largePrimeFactor(600851475143))







