pal=0
palin_list=[0]

def palindrome(n):
    rev = 0
    m=n
    while n>0:
        d=n%10
        rev=(rev*10)+d
        n=int(n/10)

    if rev==m:
        palin_list.append(rev)



for i in range(999,99,-1):
    for j in range(999,99,-1):
        m = i*j
        palindrome(m)

print(max(palin_list))




