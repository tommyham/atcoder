def probA():
    N,K=map(int, input().split())
    A=list(map(int, input().split()))
    
    for k in range(K):
        A.pop(0)
        A.append(0)
        if not len(A):
            break
    
    print(*A)

def probB():
    H,M=map(int, input().split())
    
    A=H//10
    B=H%10
    C=M//10
    D=M%10
    
    h=10*A+C
    m=10*B+D
    if h<24 and m<60:
        print(H,M)
    elif h>=24:
        print(H+1,0)
    elif m>=60:
        print(H+10-B,0)

def probC():
    N,Q=map(int, input().split())
    query=[list(map(int, input().split())) for _ in range(Q)]

    follow=dict()

    for q in query:
        if q[0]==1:
            if follow.get(q[1]):
                follow[q[1]].add(q[2])
            else:
                follow[q[1]]=set([q[2]])
        elif q[0]==2:
            follower=follow.get(q[1])
            if follower:
                if q[2] in follower:
                    follow[q[1]].remove(q[2])
                else:
                    pass
        elif q[0]==3:
            Afollower=follow.get(q[1])
            Bfollower=follow.get(q[2])
            if Afollower and Bfollower:
                if q[2] in Afollower and q[1] in Bfollower:
                    print('Yes')
                else:
                    print('No')
            else:
                print('No')

def probD():
    N=int(input())
    A=list(map(int, input().split()))
    Q=int(input())
    query=[list(map(int, input().split())) for _ in range(Q)]

    base=-1
    for q in query:
        if q[0]==1:
            base=q[1]
            change={}
        elif q[0]==2:
            if base<0:
                A[q[1]-1]+=q[2]
            else:
                if change.get(q[1]):
                    change[q[1]]+=q[2]
                else:
                    change[q[1]]=q[2]
        elif q[0]==3:
            if base<0:
                print(A[q[1]-1])
            else:
                if change.get(q[1]):
                    print(base+change[q[1]])
                else:
                    print(base)

def main():
    import numpy as np
    
    H,W,N,h,w=map(int, input().split())
    A=np.array([list(map(int, input().split())) for _ in range(H)])
    
    for k in range(H-h+1):
        for l in range(W-w+1):
            print(k,l)
    
if __name__ in '__main__':
    main()