def probA():
    import math
    N=int(input())
    if N>math.log(N**2,2):
        print("Yes")
    else:
        print("No")

def probB():
    N=int(input())
    A=list(map(int, input().split()))
    pos=0
    split=[0]*(N+2)
    for i in range(N):
        pos=(pos+A[i])%360
        split[i]=pos
    split[-1]=360
    split.sort()
    diff=[split[i+1]-split[i] for i in range(len(split)-1)]
    print(max(diff))

def probC(N):
    # N=int(input())
    n=998244353
    length=len(str(N))
    answer=0
    start=1
    for i in range(length-1):
        end=10**(i+1)-10**i
        answer+=int((end+start)*end/2)
    end=N-10**(length-1)+1
    answer+=int((end+start)*end/2)
    # print(answer%n)
    
    ans=N*(N+1)//2
    if N>=10: ans-=9*(N-9)
    if N>=100: ans-=90*(N-99)
    if N>=1000: ans-=900*(N-999)
    if N>=10000: ans-=9000*(N-9999)
    if N>=100000: ans-=90000*(N-99999)
    if N>=1000000: ans-=900000*(N-999999)
    if N>=10000000: ans-=9000000*(N-9999999)
    if N>=100000000: ans-=90000000*(N-99999999)
    if N>=1000000000: ans-=900000000*(N-999999999)
    if N>=10000000000: ans-=9000000000*(N-9999999999)
    if N>=100000000000: ans-=90000000000*(N-99999999999)
    if N>=1000000000000: ans-=900000000000*(N-999999999999)
    if N>=10000000000000: ans-=9000000000000*(N-9999999999999)
    if N>=100000000000000: ans-=90000000000000*(N-99999999999999)
    if N>=1000000000000000: ans-=900000000000000*(N-999999999999999)
    if N>=10000000000000000: ans-=9000000000000000*(N-9999999999999999)
    if N>=100000000000000000: ans-=90000000000000000*(N-99999999999999999)
    if N>=1000000000000000000: ans-=900000000000000000*(N-999999999999999999)
    # print(ans%998244353)
    
    print(answer,ans)
    print(answer%n,ans%998244353)

def probD():
    T=int(input())
    query=[list(map(int, input().split()))for _ in range(T)]
    for a,s in query:
        s-=2*a
        if s<0:
            print("No")
            continue
        if s&a==0:
            print("Yes")
        else:
            print("No")

# for i in range(9,19):
#     probC(int(str(9)*i))

N,Q=map(int, input().split())
query=[list(map(int, input().split())) for _ in range(Q)]
