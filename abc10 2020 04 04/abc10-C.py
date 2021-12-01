def absolute(N,K):
    N=abs(N-K)
    if(N<=K/2):
        pass
    else:
        N=absolute(N,K)
    return N
N,K=map(int,input().split())
N=absolute(N,K)
print(N)