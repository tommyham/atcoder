N=int(input())
P=list(map(int,input().split()))
count=0
mini=P[0]
for i in range(N):
    if(P[i]<=mini):
        mini=P[i]
        count+=1
    else:
        pass
print(count)