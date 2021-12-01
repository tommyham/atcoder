N,M=map(int,input().split())
A=list(map(int,input().split()))
ALL=sum(A)
if(ALL<=N):
    print(N-ALL)
else:
    print(-1)