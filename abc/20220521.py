def probA():
    N=int(input())
    print(chr(N))

def probB():
    N,K=map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    
    hate=[A[b-1] for b in B]
    if max(A)>max(hate):
        print("No")
    else:
        print("Yes")

def probC():
    import collections
    N=int(input())
    S=[list(str(input())) for _ in range(N)]
    
    time=[]
    for i in range(10):
        index=[s.index(str(i)) for s in S]
        c=collections.Counter(index)
        val=max(c.values())
        if val>1:
            key=max([k for k in c if c[k]==val])
            time.append(key+((val-1)*10))
        else:
            time.append(max(index))
    print(min(time))

N=int(input())
A=list(map(int, input().split()))
