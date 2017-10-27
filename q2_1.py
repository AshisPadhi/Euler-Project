s=0
def fibo(n):
    s=0
    a=0
    b=1
    c=1
    while c<n:
        c=a+b
        if c%2==0:
            s=s+c
        a=b
        b=c
    return s

print(fibo(4000000))


