n=list(map(int,input().split()))
a=n[0]
b=n[1]
k=n[2]
if(a<=k):
    k=k-a
    a=0
    if(b<=k):
        b=0
    else:
        b=b-k
else:
    a=a-k
print('{0} {1}'.format(a,b))
