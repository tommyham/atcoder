N=int(input("Please input a natural number:"))
n=list(map(int,input().split()))
print(n)
MOD=10**9+7
ans=0
square=0
for i in range(1,N):
    ans+=int(n[0])^int(n[i])
ans=(ans*ans)/2
print(int(ans%MOD))
