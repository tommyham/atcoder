def probA():
    P=list(list(map(int, input().split()))for _ in range(3))
    x,y=0,0
    if P[0][0]==P[1][0]:
        x=P[2][0]
    elif P[1][0]==P[2][0]:
        x=P[0][0]
    else:
        x=P[1][0]
        
    if P[0][1]==P[1][1]:
        y=P[2][1]
    elif P[1][1]==P[2][1]:
        y=P[0][1]
    else:
        y=P[1][1]
    
    print(x,y)

def probB():
    A,B=map(int, input().split())
    h=(A**2+B**2)**(1/2)
    print(A/h,B/h)

def probC():
    N,K,X=map(int, input().split())
    A=list(map(int, input().split()))
    q=[a//X for a in A]
    mod=[a%X for a in A]
    mod.sort(reverse=True)
    ans=0
    if sum(q)>=K:
        ans=sum(mod)+(sum(q)-K)*X
    else:
        K-=sum(q)
        if K>=len(mod):
            mod=[0]
            pass
        else:
            mod=mod[K:]
        ans=sum(mod)
    print(ans)

N=int(input())
