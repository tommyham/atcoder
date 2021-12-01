A,B,N=map(int,input().split())
ans=0
way=0
if(N<B):
    for x in range(N,N+1):
        way=(A*x)//B-A*(x//B)
        if(way>ans):
            ans=way
        else:
            pass
        way=0
else:
    for x in range(1,N,B):
        way=(A*x)//B-A*(x//B)
        if(way>ans):
            ans=way
        else:
            pass
        way=0

print(ans)