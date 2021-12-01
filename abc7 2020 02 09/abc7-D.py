N,K=map(int,input().split())
p=list(map(int,input().split()))
ans=sum(p[0:K])
all_sum=[sum(p[0:K])]
for i in range(len(p)-K):
    ans=ans+p[i+K]-p[i]
    all_sum.append(ans)
ans=max(all_sum)
print((ans+K)/2)