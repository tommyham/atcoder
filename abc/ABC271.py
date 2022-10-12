def probA():
    N=int(input())
    N=hex(N).replace('0x','').upper()
    print(N.zfill(2))

def probB():
    N,Q=map(int, input().split())
    L=[list(map(int, input().split())) for _ in range(N)]
    query=[list(map(int, input().split())) for _ in range(Q)]
    
    for q in query:
        print(L[q[0]-1][q[1]])

N=int(input())
A=sorted(list(map(int, input().split())))

mod=0
buy=0
read=0

for i in range(len(A)):
    if A[i]==read+1:
        read+=1
    elif A[i]==read:
        mod+=1
        if i==len(A)-1:
            read+=max(0,mod//2-buy)
    else:
        buy+=A[i]-read-1
        if buy<=(len(A[i+1:])+mod)//2:
            read=A[i]
        else:
            read+=max(0,(len(A[i:])+mod)//2-(buy-(A[i]-read-1)))
            break

print(read)