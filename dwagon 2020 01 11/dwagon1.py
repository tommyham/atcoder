N=int(input())
S=[0]*N
T=[0]*N
for i in range(N):
    S[i],T[i]=input().split()
    T[i]=int(T[i])
X=str(input())
count=0
for i in S:
    count+=1
    if(X==i):
        break
    else:
        pass
print(sum(T[count:N]))