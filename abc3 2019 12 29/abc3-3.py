n=int(input())
t=0
count=0
if n!=2:
    while t==0:
        for i in range(2,n):
            if n%i==0:
                count+=1
                break
            else:
                pass
        if count==0:
            break
        else:
            count=0
            n=n+1
else:
    pass
print(n)
