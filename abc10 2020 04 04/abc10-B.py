N,M=map(int,input().split())
A=list(map(int,input().split()))
ALL=sum(A)
ave=ALL/(4*M)
count=0
for i in range(N):
    if(A[i]>=ave):
        count+=1
    else:
        pass
if(count>=M):
    print("Yes")
else:
    print("No")