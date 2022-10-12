N,K=map(int, input().split())
A=list(map(int, input().split()))
front=A[:K]
front.reverse()
back=A[K:]
q=[0,0]
ans=-1
judge=False
while q[0]<len(front) or q[1]<len(back):
    while q[0]>=0 and q[1]<len(back):
        if back[q[1]]-front[q[0]]>0:
            ans=sum(q)+1
            break
        q[0]-=1
        q[1]+=1
    if q[0]<0:
        q[0]=0
    

print(ans)