def probA():
    A,B=map(int, input().split())
    point=[4,2,1]
    
    p_a=[0,0,0]
    p_b=[0,0,0]
    for i in range(len(point)):
        p=point[i]
        if A>=p:
            A-=p
            p_a[i]=1
        else:
            pass
    
    for i in range(len(point)):
        p=point[i]
        if B>=p:
            B-=p
            p_b[i]=1
        else:
            pass
    
    ans=0
    for i in range(len(point)):
        if p_a[i] or p_b[i]:
            ans+=point[i]
        else:
            pass
    print(ans)

def probB():
    X,Y,Z=map(int, input().split())
    
    if abs(X)<abs(Y):
        print(abs(X))
    elif X*Y<0:
        print(abs(X))
    elif Z*Y<0:
        print(abs(2*Z)+abs(X))
    elif abs(Z)<abs(Y):
        print(abs(X))
    else:
        print(-1)

N,X,Y=map(int, input().split())
path=[list(map(int, input().split())) for _ in range(N)]
