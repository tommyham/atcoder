def probA():
    X,Y,N=map(int, input().split())
    
    if X<Y/3:
        print(int(N*X))
    else:
        print(int(N//3*Y+N%3*X))

def probB():
    N,M,T=map(int, input().split())
    A=list(map(int, input().split()))
    bonus=[list(map(int, input().split())) for _ in range(M)]
    
    judge=True
    for n in range(N-1):
        if len(bonus):
            if bonus[0][0]==n+1:
                T+=bonus.pop(0)[1]
        
        T-=A[n]
        
        if T<=0:
            judge=False
            break
    
    if judge:
        print("Yes")
    else:
        print("No")

def probC():
    H,W=map(int, input().split())
    G=[str(input()) for _ in range(H)]
    
    i,j=0,0
    root=set()
    root.add(str(000)+str(000))
    while True:
        s=G[i][j]
        
        if s=="U" and i!=0:
            i-=1
        elif s=="D" and i!=H-1:
            i+=1
        elif s=="L" and j!=0:
            j-=1
        elif s=="R" and j!=W-1:
            j+=1
        else:
            print(i+1,j+1)
            break
        
        if str(i).zfill(3)+str(j).zfill(3) in root:
            print(-1)
            break
        
        root.add(str(i).zfill(3)+str(j).zfill(3))

import itertools
N,P,Q,R=map(int, input().split())
A=list(map(int, input().split()))

num=[i for i in range(N+1)]
combo=[c for c in itertools.combinations(num,4)]

judge=False
i=0
c=combo[0]
Sp=sum(A[c[0]:c[1]])
Sq=sum(A[c[1]:c[2]])
Sr=sum(A[c[2]:c[3]])
while i<len(combo):
    c=combo[i]
    if Sp!=P:
        plen=int((N-c[1])*(N-1-c[1])/2)
        i+=plen
        Sp=sum(A[c[0]:c[1]])
        Sq=sum(A[c[1]:c[2]])
        Sr=sum(A[c[2]:c[3]])
    elif Sq!=Q:
        qlen=N-c[2]
        i+=qlen
        Sq=sum(A[c[1]:c[2]])
        Sr=sum(A[c[2]:c[3]])
    elif Sr!=R:
        i+=1
        Sr=sum(A[c[2]:c[3]])
    else:
        judge=True
        break

if judge:
    print("Yes")
else:
    print("No")