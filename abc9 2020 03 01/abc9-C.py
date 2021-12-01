N,M=map(int,input().split())
S=[0 for i in range(M)]
C=[0 for i in range(M)]
for i in range(M):
    S[i],C[i]=map(int,input().split())
ans=0
way=[0 for i in range(N)]
judge="True"
if(max(S)<=N):
    for i in range(M):
        for j in range(i,M):
            if(S[i]==S[j] and C[i]!=C[j]):
                judge="False"
                break
            else:
                pass
        if(judge=="False"):
            break
        else:
            pass
    if(judge=="False"):
        ans=-1
    else:
        for i in range(M):
            way[S[i]-1]=C[i]
        if(way[0]!=0):
            for i in range(N):
                ans+=way[i]*(10**(N-1-i))
        else:
            ans=-1  
else:
    ans=-1
print(ans)