def probA():
    N=int(input())
    A=list(map(int, input().split()))
    print(sum(A))

def probB():
    N,M=map(int, input().split())
    entry=[list(map(int, input().split())) for _ in range(M)]
    
    judge=[[0 for _ in range(N)] for _ in range(N)]
    for e in entry:
        for i in range(1,len(e)):
            for j in range(i+1,len(e)):
                judge[e[i]-1][e[j]-1]=1
                judge[e[j]-1][e[i]-1]=1
    
    flag=True
    for j in judge:
        if sum(j)==N-1:
            continue
        else:
            flag=False
            break
        
    if flag:
        print('Yes')
    else:
        print('No')

def probC():
    N=int(input())
    A=list(map(int, input().split()))
    
    odd=[]
    even=[]
    for a in A:
        if a%2:
            odd.append(a)
            odd.sort()
            if len(odd)>2:
                odd.pop(0)
        else:
            even.append(a)
            even.sort()
            if len(even)>2:
                even.pop(0)
    
    if len(odd)==2 or len(even)==2:
        print(max(sum(odd),sum(even)))
    else:
        print(-1)

N,M=map(int, input().split())
