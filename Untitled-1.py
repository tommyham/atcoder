N=int(input("Please input a natural number:"))
n=list(map(int,input().split()))
print(n)
MOD=10**9+7
ans=0
count=[]
sell=[0,0]
for j in range(60):
    for i in range(N):
        if ((n[i]>>j)%2)==1:
            sell[1]+=1
        else:
            sell[0]+=1
    count.append(sell)
    sell=[0,0]
for i in range(len(count)):
    ans+=(count[i][0]*count[i][1])*2**i
print(int(ans%MOD))