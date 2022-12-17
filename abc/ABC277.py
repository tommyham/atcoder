def probA():
    N,X=map(int, input().split())
    P=list(map(int, input().split()))
    
    for i in range(len(P)):
        if P[i]==X:
            print(i+1)

def probB():
    N=int(input())
    S=[str(input()) for _ in range(N)]
    
    first=set(['H','D','C','S'])
    second=set(['A','2','3','4','5','6','7','8','9','T','J','Q','K'])
    
    check=True
    if len(set(S))==N:
        for s in S:
            if (s[0] in first) and (s[1] in second):
                pass
            else:
                check=False
                break
    else:
        check=False
    
    if check:
        print('Yes')
    else:
        print('No')

N=int(input())
ladders=dict()
for _ in range(N):
    A,B=map(int, input().split())
    if ladders.get(A):
        ladders[A].add(B)
    else:
        ladders[A]=set([B])
    
    if ladders.get(B):
        ladders[B].add(A)
    else:
        ladders[B]=set([A])

def checkStep(lad,step=1,root=set([1])):
    ans=step
    ladder=lad.get(step)
    if ladder==None:
        return ans
    for l in ladder:
        if l in root:
            continue
        else:
            root.add(l)
            height=checkStep(lad,step=l,root=root)
            root.remove(l)
            if height>ans:
                ans=height
    
    return ans
print(checkStep(ladders))