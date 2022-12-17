def probA():
    S=str(input())
    ans=False
    for i in range(len(S)):
        if S[i]=='a':
            ans=i+1
        else:
            pass
    
    if ans:
        print(ans)
    else:
        print(-1)

def probB():
    N,M=map(int,input().split())
    query=[list(map(int,input().split())) for _ in range(M)]
    query=sorted(query, key=lambda x: x[0])
    
    citeis=[[] for _ in range(N)]
    center=1
    for q in query:
        citeis[q[0]-1].append(q[1])
        citeis[q[1]-1].append(q[0])
    
    for c in citeis:
        if len(c):
            print(len(c),*sorted(c))
        else:
            print(0)

def probC():
    N=int(input())
    P=list(map(int,input().split()))
    
    index=len(P)
    for i in range(1,len(P)):
        if P[-i]>P[-i-1]:
            pass
        else:
            index=i+1
            break
    
    forward=P[:-index] # 固定
    back=P[-index:] # 入れ換え対象
    head=max([b for b in back if b<back[0]])
    back.remove(head)
    print(*(forward+[head]+sorted(back,reverse=True)))

N=int(input())
A=set(map(int, input().split()))
twice=[a for a in A if (not a%2)and(a%3)]
third=[a for a in A if (a%2)and(not a%3)]
both=[a for a in A if (not a%2)and(not a%3)]
neither=[a for a in A if (a%2)and(a%3)]

if len(neither)>1:
    print(-1)