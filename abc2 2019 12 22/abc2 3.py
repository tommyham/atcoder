N=list(map(int,input().split()))
m=int(N[0])
n=int(N[1])
ans=1
while(ans!=0):
    ans=m%n
    if(ans<n and ans!=0):
        m=n
        n=ans
    else:
        pass
print(int((N[0]*N[1])/n))
