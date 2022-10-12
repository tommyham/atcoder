def probA():
    S=str(input())
    week=['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday' ]
    print(5-week.index(S))

def probB():
    S=str(input())
    
    line=[0 for _ in range(7)]
    lane=[3,2,4,1,3,5,0,2,4,6]
    
    for i,s in enumerate(S):
        if int(s):
            line[lane[i]]+=1
    
    if int(S[0]):
        print('No')
    else:
        split=False
        judge=False
        pre=0
        for l in line:
            if l:
                if judge:
                    split=True
                    break
            elif pre:
                judge=True
            pre=l
        if split:
            print('Yes')
        else:
            print('No')

def probC():
    N,M=map(int, input().split())
    A=list(map(int, input().split()))
    
    ans=sum([(i+1)*a for i,a in enumerate(A[:M])])
    
    partial=ans
    fare=sum(A[1:M])
    pre_a=A[0]
    
    for i,a in enumerate(A[M:]):
        partial+=a*M-pre_a-fare
    
        if partial>ans:
            ans=partial
        
        pre_a=A[i+1]
        fare+=a-pre_a
    
    print(ans)

import itertools
N,M=map(int, input().split())
A=list(map(int, input().split()))

num=[i for i in range(N)]
combo=[c for c in itertools.combinations(num,M)]

ans=sum([(i+1)*a for i,a in enumerate(A[:M])])

for c in combo[1:]:
    partial=0
    for i in range(M):
        partial+=A[c[i]]*(i+1)
    
        if partial>ans:
            ans=partial
print(ans)