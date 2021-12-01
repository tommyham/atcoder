N=int(input())
s=list(input().split())
ans=str()
for i in range(N):
    ans+=s[0][i]+s[1][i]
print(ans)
