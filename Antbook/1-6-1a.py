import math
N=int(input())
x=[0 for i in range(N)]
y=[0 for i in range(N)]
for i in range(N):
    x[i],y[i]=map(int,input().split())
ans=0
com=0
for i in range(N):
    for j in range(i,N):
        com=math.sqrt(abs(x[i]-x[j])**2+abs(y[i]-y[j])**2)
        if(com>ans):
            ans=com
        else:
            pass
print(ans)