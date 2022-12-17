def probA():
    def factorial(x):
        if x==0:
            return 1
        else:
            return x*factorial(x-1)
    
    N=int(input())
    print(factorial(N))

def probB():
    import sys
    N,K=map(int, input().split())
    N=list(map(int,list(str(N))))
    
    if len(N)+1<=K:
        print(0)
        sys.exit()
    
    for k in range(K):
        if N[-k-1]<5:
            pass
        else:
            if k<len(N)-1:
                N[-k-2]+=1
            else:
                N=[1]+N
        N[-k-1]=0
    
    ans=0
    for i in range(len(N)):
        ans+=N[-i-1]*10**(i)
    print(ans)

N=int(input())
A=list(map(int, input().split()))
