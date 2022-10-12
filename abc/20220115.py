def probA():
    N=str(input())
    ans=0
    for i in N:
        ans+=int(i)
    print(ans*100+ans*10+ans)

def probB():
    N=int(input())
    H=list(map(int,input().split()))
    hight=H[0]
    for i in H[1:]:
        if i>hight:
            hight=i
        else:
            break
    print(hight)

N,Q=map(int,input().split())
A=list(map(int,input().split()))
E=[i+1 for i in range(N)]
X=[0]*Q
K=[0]*Q
for i in range(Q):
    X[i],K[i]=map(int, input().split())
zipList=zip(A,E)
zipSort=sorted(zipList,reverse=True)
A,E=zip(*zipSort)
zipList=zip(X,K)
zipSort=sorted(zipList,reverse=True)
X,K=zip(*zipSort)
count=0
for x,k in zip(X,K):
    if A[count]==x:
        